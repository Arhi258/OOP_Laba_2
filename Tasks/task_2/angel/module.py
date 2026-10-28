#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


class Angel:
    def __init__(self, degrees, minutes):
        if type(degrees) is not int or type(minutes) is not int:
            raise ValueError("Градусы и минуты должны быть целыми числами.")

        if not 0 <= minutes < 60:
            raise ValueError("Минуты должны быть от 0 до 59.")

        if degrees < 0:
            self.total_minutes = degrees * 60 - minutes
        else:
            self.total_minutes = degrees * 60 + minutes

    @staticmethod
    def read():
        degrees = int(input("Введите градусы: "))
        minutes = int(input("Введите минуты: "))
        return degrees, minutes

    def display(self):
        sign = "-" if self.total_minutes < 0 else ""
        degrees, minutes = divmod(abs(self.total_minutes), 60)
        print(f"Угол: {sign}{degrees}° {minutes}′")

    def to_radians(self):
        return math.radians(self.total_minutes / 60)

    def normalize(self):
        self.total_minutes %= 360 * 60

    def increase(self, degrees, minutes):
        if type(degrees) is not int or degrees < 0:
            raise ValueError(
                "Добавляемые градусы должны быть целым неотрицательным числом."
            )

        amount = Angel(degrees, minutes)
        self.total_minutes += amount.total_minutes

    def decrease(self, degrees, minutes):
        if type(degrees) is not int or degrees < 0:
            raise ValueError(
                "Вычитаемые градусы должны быть целым неотрицательным числом."
            )

        amount = Angel(degrees, minutes)
        self.total_minutes -= amount.total_minutes

    def sine(self):
        return math.sin(self.to_radians())

    def compare(self, other):
        if not isinstance(other, Angel):
            raise ValueError("Для сравнения нужен объект Angel.")

        first = self.total_minutes % (360 * 60)
        second = other.total_minutes % (360 * 60)

        if first > second:
            return 1
        if first < second:
            return -1
        return 0
