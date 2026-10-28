#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

from Tasks.task_1.make_pair import make_pair
from Tasks.task_1.pair import Pair


def test_cost():
    product = make_pair(12.5, 4)
    assert product.cost() == 50.0


def test_fields():
    product = Pair(20, 3)
    assert product.first == 20.0
    assert product.second == 3


@pytest.mark.parametrize(
    "price, quantity",
    [
        (0, 1),
        (-2, 1),
        (10, 0),
        (10, -2),
        (10, 2.5),
    ],
)
def test_invalid_values(price, quantity):
    with pytest.raises(SystemExit):
        make_pair(price, quantity)


def test_read(monkeypatch):
    answers = iter(["25.5", "2"])
    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(answers),
    )

    assert Pair.read() == (25.5, 2)


def test_display(capsys):
    Pair(3.5, 2).display()
    output = capsys.readouterr().out

    assert "Цена: 3.50" in output
    assert "Количество: 2" in output
