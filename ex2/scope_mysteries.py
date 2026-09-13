from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable:
    count = 0

    def step() -> int:
        nonlocal count
        count += 1
        return count

    return step


def spell_accumulator(initial_power: int) -> Callable:
    total = initial_power

    def add(amount: int) -> int:
        nonlocal total
        total += amount
        return total

    return add


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchant(item: str) -> str:
        return f"{enchantment_type} {item}"

    return enchant


def memory_vault() -> dict[str, Callable]:
    memories: dict = {}

    def store(key: str, value: Any) -> None:
        memories[key] = value

    def recall(key: str) -> Any:
        return memories.get(key, "Memory not found")

    return {"store": store, "recall": recall}


def main() -> None:
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print("counter_a call 1:", counter_a())
    print("counter_a call 2:", counter_a())
    print("counter_b call 1:", counter_b())

    print()
    print("Testing spell accumulator...")
    power = spell_accumulator(100)
    print("Base 100, add 20:", power(20))
    print("Base 100, add 30:", power(30))

    print()
    print("Testing enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Shield"))

    print()
    print("Testing memory vault...")
    vault = memory_vault()
    vault["store"]("secret", 42)
    vault["store"]("element", "fire")
    vault["store"]("spells", ["heal", "shield"])
    print("Recall 'secret':", vault["recall"]("secret"))
    print("Recall 'element':", vault["recall"]("element"))
    print("Recall 'spells':", vault["recall"]("spells"))
    print("Recall 'unknown':", vault["recall"]("unknown"))


if __name__ == "__main__":
    main()
