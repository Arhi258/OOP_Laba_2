#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


class Pair:
    def __init__(self, first, second):
        if (
            isinstance(first, bool)
            or not isinstance(first, (int, float))
            or not math.isfinite(first)
            or first <= 0
        ):
            raise ValueError("Цена должна быть положительным числом.")

        if type(second) is not int or second <= 0:
            raise ValueError("Количество должно быть положительным целым числом.")

        self.first = float(first)
        self.second = second

    @staticmethod  # read() можно вызвать через класс
    def read():
        first = float(input("Введите цену товара: "))
        second = int(input("Введите количество товара: "))
        return first, second

    def display(self):
        print(f"Цена: {self.first:.2f}")
        print(f"Количество: {self.second}")

    def cost(self):
        return self.first * self.second
