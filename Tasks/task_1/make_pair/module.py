#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Tasks.task_1.pair import Pair


def make_pair(first, second):
    try:
        return Pair(first, second)
    except ValueError as error:
        print(f"Ошибка: {error}")
        raise SystemExit(1) from None
