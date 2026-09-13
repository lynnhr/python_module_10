import time
from collections.abc import Callable
from functools import wraps
from typing import Any


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Spell completed in {time.time() - start:.3f} seconds")
        return result

    return wrapper


def power_validator(min_power: int) -> Callable[
        [Callable[..., Any]], Callable[..., Any]]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            power = kwargs["power"] if "power" in kwargs else args[-1]
            if power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> Callable[
        [Callable[..., Any]], Callable[..., Any]]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
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


def make_flaky_spell() -> Callable[..., Any]:
    attempts = 0

    @retry_spell(3)
    def flaky_spell() -> str:
        nonlocal attempts
        attempts += 1
        if attempts < 3:
            raise ValueError("the magic is unstable")
        return "Flaky spell worked on attempt 3!"

    return flaky_spell


def main() -> None:
    print("Testing spell timer...")
    print("Result:", fireball())

    print()
    print("Testing retrying spell...")
    print(cursed_spell())
    print(waaagh_spell())
    print(make_flaky_spell()())

    print()
    print("Testing functools.wraps...")
    print("Name kept:", fireball.__name__)

    print()
    print("Testing MageGuild...")
    guild = MageGuild()
    print(MageGuild.validate_mage_name("Alex"))
    print(MageGuild.validate_mage_name("A1"))
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Spark", 5))


if __name__ == "__main__":
    main()
