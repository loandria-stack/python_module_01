#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plant_growth.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: loandria <loandria@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/01 13:02:05 by loandria            #+#    #+#            #
#   Updated: 2026/05/26 12:58:25 by loandria           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self, grow: float) -> None:
        self.height = self.height + grow

    def Age(self) -> None:
        self.age = self.age + 1

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")


def ft_plant_growth() -> None:
    print("=== Garden Plant Growth ===")
    rose = Plant("Rose", 25.0, 30)
    rose.show()
    first_height = rose.height
    for days in range(1, 8):
        print(f"=== Day {days} ===")
        rose.grow(0.8)
        rose.Age()
        rose.show()
    new_height = rose.height
    total_height = round((new_height - first_height), 1)
    print(f"Growth this week: {total_height}")


if __name__ == "__main__":
    ft_plant_growth()
