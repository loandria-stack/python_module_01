#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plant_types.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: loandria <loandria@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/05 00:11:24 by loandria            #+#    #+#            #
#   Updated: 2026/06/04 11:18:57 by loandria           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age

    def grow(self, grow: float) -> None:
        self._height = self._height + grow

    def Age(self) -> None:
        self._age = self._age + 1

    def show(self) -> None:
        print(
            f"{self._name}: {round(self._height, 1)}cm, {self._age} days old"
            )


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.is_bloomed = False

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.is_bloomed:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")

    def bloom(self) -> None:
        self.is_bloomed = True


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 age: int, diameter: float) -> None:
        super().__init__(name, height, age)
        self.diameter = diameter

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.diameter}cm")

    def produce_shade(self) -> None:
        print("[asking the oak to produce shade]")
        print(f"Tree Oak now produces a shade of {self._height}cm", end=" ")
        print(f"long and {self.diameter}cm wide.")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int, season: str,
                 nutritional_value: int) -> None:
        super().__init__(name, height, age)
        self.season = season
        self.nutritional_value = nutritional_value

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.season}")
        print(f"Nutritional value: {self.nutritional_value}")

    def grow_and_age(self, days: int, growing: float) -> None:
        for i in range(days):
            super().grow(growing)
            super().Age()
            self.nutritional_value += 1


def ft_plant_types() -> None:
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    oak.produce_shade()
    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April", 0)
    tomato.show()
    days = 20
    print(f"[make tomato grow and age for {days} days]")
    tomato.grow_and_age(days, 2.1)
    tomato.show()


if __name__ == "__main__":
    ft_plant_types()
