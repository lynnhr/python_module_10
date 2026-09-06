import time
from collections.abc import Callable
from functools import wraps


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Spell completed in {time.time() - start:.3f} seconds")
        return result

    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            power = kwargs["power"] if "power" in kwargs else args[-1]
            if power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(f"Spell failed, retrying... "
                              f"(attempt {attempt}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"

        return wrapper

    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        letters_only = all(c.isalpha() or c.isspace() for c in name)
        return len(name) >= 3 and letters_only

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


@spell_timer
def fireball() -> str:
    time.sleep(0.1)
    return "Fireball cast!"


@retry_spell(3)
def cursed_spell() -> str:
    raise ValueError("the magic is unstable")


@retry_spell(3)
def waaagh_spell() -> str:
    return "Waaaaaaagh spelled !"


def main() -> None:
    print("Testing spell timer...")
    print("Result:", fireball())

    print()
    print("Testing retrying spell...")
    print(cursed_spell())
    print(waaagh_spell())

    print()
    print("Testing MageGuild...")
    guild = MageGuild()
    print(MageGuild.validate_mage_name("Alex"))
    print(MageGuild.validate_mage_name("A1"))
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Spark", 5))


if __name__ == "__main__":
    main()
