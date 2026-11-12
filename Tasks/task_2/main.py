#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Составить программу с использованием классов и объектов
# для решения задачи.
#
# Во всех заданиях, помимо указанных в задании операций,
# обязательно должны быть реализованы следующие методы:
# метод инициализации __init__; ввод с клавиатуры read;
# вывод на экран display.
#
# В раздел программы, начинающийся после инструкции
# if __name__ == "__main__": добавить код, демонстрирующий
# возможности разработанного класса.
#
# Создать класс Angel для работы с углами на плоскости,
# задаваемыми величиной в градусах и минутах.
#
# Обязательно должны быть реализованы:
# перевод в радианы, приведение к диапазону 0–360 градусов,
# увеличение и уменьшение угла на заданную величину,
# получение синуса, сравнение углов.

from Tasks.task_2.angel import Angel


def main():
    try:
        degrees, minutes = Angel.read()
        angle = Angel(degrees, minutes)

        angle.display()
        print(f"В радианах: {angle.to_radians():.4f}")
        print(f"Синус угла: {angle.sine():.4f}")

        angle.normalize()
        print("После приведения к диапазону 0–360°:")
        angle.display()

        print("Увеличение угла:")
        degrees = int(input("Введите градусы: "))
        minutes = int(input("Введите минуты: "))
        angle.increase(degrees, minutes)
        angle.display()

        print("Уменьшение угла:")
        degrees = int(input("Введите градусы: "))
        minutes = int(input("Введите минуты: "))
        angle.decrease(degrees, minutes)
        angle.display()

        print("Введите второй угол для сравнения:")
        degrees, minutes = Angel.read()
        other = Angel(degrees, minutes)

        result = angle.compare(other)

        if result > 0:
            print("Первый угол больше второго.")
        elif result < 0:
            print("Первый угол меньше второго.")
        else:
            print("Углы равны.")

    except ValueError as error:
        print(f"Ошибка: {error}")
        raise SystemExit(1) from None


if __name__ == "__main__":
    main()
