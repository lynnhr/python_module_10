from typing import Any


def artifact_sorter(artifacts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(artifacts, key=lambda a: a["power"], reverse=True)


def power_filter(mages: list[dict[str, Any]],
                 min_power: int) -> list[dict[str, Any]]:
    return list(filter(lambda m: m["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, Any]:
    if not mages:
        return {"max_power": 0, "min_power": 0, "avg_power": 0.0}
    powers = list(map(lambda m: m["power"], mages))
    return {
        "max_power": max(mages, key=lambda m: m["power"])["power"],
        "min_power": min(mages, key=lambda m: m["power"])["power"],
        "avg_power": round(sum(powers) / len(powers), 2),
    }


def main() -> None:
    artifacts = [
        {"name": "Crystal Orb", "power": 85, "type": "focus"},
        {"name": "Fire Staff", "power": 92, "type": "weapon"},
        {"name": "Ice Wand", "power": 70, "type": "weapon"},
    ]
    mages = [
        {"name": "Alex", "power": 88, "element": "fire"},
        {"name": "Jordan", "power": 61, "element": "ice"},
        {"name": "Riley", "power": 95, "element": "shadow"},
    ]
    spells = ["fireball", "heal", "shield"]

    try:
        print("Testing artifact sorter...")
        ranked = artifact_sorter(artifacts)
        first, second = ranked[0], ranked[1]
        print(f"{first['name']} ({first['power']} power) comes before "
              f"{second['name']} ({second['power']} power)")

        print()
        print("Testing power filter...")
        strong = power_filter(mages, 80)
        print(", ".join(map(lambda m: m["name"], strong)))

        print()
        print("Testing spell transformer...")
        print(" ".join(spell_transformer(spells)))

        print()
        print("Testing mage stats...")
        print(mage_stats(mages))
    except (KeyError, TypeError, IndexError) as error:
        print(f"The spell fizzled: {error}")


if __name__ == "__main__":
    main()
