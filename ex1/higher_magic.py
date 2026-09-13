from collections.abc import Callable


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def shield(target: str, power: int) -> str:
    return f"Shield protects {target} with {power} points"


def spell_combiner(spell1: Callable[[str, int], str],
                   spell2: Callable[[str, int], str]
                   ) -> Callable[[str, int], tuple[str, str]]:
    if not callable(spell1) or not callable(spell2):
        raise TypeError("spell_combiner needs two spells")

    def combined(target: str, power: int) -> tuple[str, str]:
        return spell1(target, power), spell2(target, power)

    return combined


def power_amplifier(base_spell: Callable[[str, int], str],
                    multiplier: int) -> Callable[[str, int], str]:
    if not callable(base_spell):
        raise TypeError("power_amplifier needs a spell")

    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)

    return amplified


def conditional_caster(condition: Callable[[str, int], bool],
                       spell: Callable[[str, int], str]
                       ) -> Callable[[str, int], str]:
    if not callable(condition) or not callable(spell):
        raise TypeError("conditional_caster needs a condition and a spell")

    def guarded(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"

    return guarded


def spell_sequence(spells: list[Callable[[str, int], str]]
                   ) -> Callable[[str, int], list[str]]:
    if not all(callable(spell) for spell in spells):
        raise TypeError("spell_sequence needs a list of spells")

    def cast_all(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]

    return cast_all


def main() -> None:
    try:
        print("Testing spell combiner...")
        combined = spell_combiner(fireball, heal)
        print("Combined spell result:", ", ".join(combined("Dragon", 10)))

        print()
        print("Testing power amplifier...")
        mega_fireball = power_amplifier(fireball, 3)
        print("Original:", fireball("Dragon", 10))
        print("Amplified:", mega_fireball("Dragon", 10))

        print()
        print("Testing conditional caster...")
        strong_only = conditional_caster(lambda t, p: p >= 50, fireball)
        print("Power 80 ->", strong_only("Dragon", 80))
        print("Power 20 ->", strong_only("Dragon", 20))

        print()
        print("Testing spell sequence...")
        barrage = spell_sequence([fireball, heal, shield])
        for result in barrage("Dragon", 25):
            print(" -", result)

        print()
        print("Testing composition...")
        combo = spell_sequence([mega_fireball, strong_only])
        for result in combo("Golem", 60):
            print(" -", result)
    except TypeError as error:
        print(f"The spell fizzled: {error}")


if __name__ == "__main__":
    main()
