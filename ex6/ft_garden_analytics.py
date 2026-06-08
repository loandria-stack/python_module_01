#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_garden_analytics.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: loandria <loandria@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/04 21:07:52 by loandria            #+#    #+#            #
#   Updated: 2026/06/04 22:01:45 by loandria           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    class _Stats:
        def __init__(self) -> None:
            self._stats_grow: int = 0
            self._stats_age: int = 0
            self._stats_show: int = 0

        def stats_of_grow(self) -> None:
            self._stats_grow += 1

        def stats_of_age(self) -> None:
            self._stats_age += 1

        def stats_of_show(self) -> None:
            self._stats_show += 1

        def show_stats(self, plant_name: str) -> None:
            print(f"[statistics for {plant_name}]")
            print(
                f"Stats: {self._stats_grow} grow, "
                f"{self._stats_age} age, "
                f"{self._stats_show} show"
            )

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = round(height, 1)
        self._age = age
        self.stats = Plant._Stats()

    def grow(self, amount: float) -> None:
        self._height = round(self._height + amount, 1)
        self.stats.stats_of_grow()

    def age(self, days: int) -> None:
        self._age += days
        self.stats.stats_of_age()

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age} days old")
        self.stats.stats_of_show()

    @staticmethod
    def is_more_than_a_year(days: int) -> bool:
        return days > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._bloomed = False

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if self._bloomed:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")

    def bloom(self) -> None:
        self._bloomed = True


class Tree(Plant):
    class _TreeStats(Plant._Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_count: int = 0

        def shade_stats(self) -> None:
            self._shade_count += 1

        def show_stats(self, plant_name: str) -> None:
            super().show_stats(plant_name)
            print(f"{self._shade_count} shade")

    def __init__(
        self, name: str, height: float, age: int, diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self._diameter = diameter
        self.stats: Tree._TreeStats = Tree._TreeStats()

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._diameter}cm")

    def produce_shade(self) -> None:
        print(
            f"Tree {self._name} now produces a shade of "
            f"{self._height}cm long and {self._diameter}cm wide."
        )
        self.stats.shade_stats()


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self._seeds = 0

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seeds}")

    def grow_age_and_bloom(
        self, days: int, grow_per_day: float, seeds_produced: int
    ) -> None:
        total_growth: float = 0
        for _ in range(days):
            total_growth += grow_per_day
        self.grow(round(total_growth, 1))
        self.age(days)
        self.bloom()
        self._seeds = seeds_produced


def show_plant_stats(plant: Plant) -> None:
    plant.stats.show_stats(plant._name)


def ft_plant_types() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(
        f"Is 30 days more than a year? -> "
        f"{Plant.is_more_than_a_year(30)}"
    )
    print(
        f"Is 400 days more than a year? -> "
        f"{Plant.is_more_than_a_year(400)}"
    )

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    show_plant_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(8.0)
    rose.bloom()
    rose.show()
    show_plant_stats(rose)

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    show_plant_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    show_plant_stats(oak)

    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow_age_and_bloom(
        days=20, grow_per_day=1.5, seeds_produced=42
    )
    sunflower.show()
    show_plant_stats(sunflower)

    print("=== Anonymous")
    unknown = Plant.create_anonymous()
    unknown.show()
    show_plant_stats(unknown)


if __name__ == "__main__":
    ft_plant_types()
