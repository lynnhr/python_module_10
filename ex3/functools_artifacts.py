import operator
from collections.abc import Callable
from functools import lru_cache, partial, reduce, singledispatch
from typing import Any

OPERATIONS = {
    "add": operator.add,
    "multiply": operator.mul,
    "max": max,
    "min": min,
}


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    if operation not in OPERATIONS:
        raise ValueError(f"Unknown operation: {operation}")
    return reduce(OPERATIONS[operation], spells)


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"{element.title()} {target} ({power} power)"


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    if not callable(base_enchantment):
        raise TypeError("partial_enchanter needs an enchantment function")
    return {
        "fire": partial(base_enchantment, 50, "flaming"),
        "ice": partial(base_enchantment, 50, "frozen"),
        "lightning": partial(base_enchantment, 50, "shocking"),
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("fibonacci needs a positive number")
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def cast(spell: Any) -> str:
        return "Unknown spell type"

    @cast.register
    def cast_damage(spell: int) -> str:
        return f"{spell} damage"

    @cast.register
    def cast_enchantment(spell: str) -> str:
        return spell

    @cast.register
    def cast_multi(spell: list) -> str:
        return f"{len(spell)} spells"

    return cast


def main() -> None:
    spells = [10, 20, 30, 40]
    try:
        print("Testing spell reducer...")
        print("Sum:", spell_reducer(spells, "add"))
        print("Product:", spell_reducer(spells, "multiply"))
        print("Max:", spell_reducer(spells, "max"))
        print("Empty:", spell_reducer([], "add"))

        print()
        print("Testing partial enchanter...")
        enchanters = partial_enchanter(base_enchantment)
        print(enchanters["fire"]("Sword"))
        print(enchanters["ice"]("Shield"))

        print()
        print("Testing memoized fibonacci...")
        for number in (0, 1, 10, 15):
            print(f"Fib({number}):", memoized_fibonacci(number))
        print("Cache:", memoized_fibonacci.cache_info())

        print()
        print("Testing spell dispatcher...")
        cast = spell_dispatcher()
        print("Damage spell:", cast(42))
        print("Enchantment:", cast("fireball"))
        print("Multi-cast:", cast(["fireball", "heal", "shield"]))
        print(cast(3.5))
    except (TypeError, ValueError) as error:
        print(f"The spell fizzled: {error}")


if __name__ == "__main__":
    main()
