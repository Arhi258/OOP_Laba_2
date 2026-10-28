#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Tasks.task_1.make_pair import make_pair
from Tasks.task_1.pair import Pair


def main():
    try:
        first, second = Pair.read()
    except ValueError:
        print("Ошибка: цена должна быть числом, а количество — целым числом.")
        raise SystemExit(1) from None

    product = make_pair(first, second)
    product.display()
    print(f"Стоимость товара: {product.cost():.2f}")


if __name__ == "__main__":
    main()
