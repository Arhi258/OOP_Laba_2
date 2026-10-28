#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

import pytest

from Tasks.task_2.angel import Angel


def test_radians():
    assert Angel(180, 0).to_radians() == pytest.approx(math.pi)


def test_normalize():
    angle = Angel(390, 30)
    angle.normalize()
    assert angle.total_minutes == 30 * 60 + 30


def test_normalize_negative():
    angle = Angel(-30, 0)
    angle.normalize()
    assert angle.total_minutes == 330 * 60


def test_increase():
    angle = Angel(30, 15)
    angle.increase(10, 30)
    assert angle.total_minutes == 40 * 60 + 45


def test_decrease():
    angle = Angel(50, 30)
    angle.decrease(10, 45)
    assert angle.total_minutes == 39 * 60 + 45


def test_sine():
    assert Angel(30, 0).sine() == pytest.approx(0.5)


def test_compare():
    assert Angel(90, 0).compare(Angel(45, 0)) == 1
    assert Angel(30, 0).compare(Angel(60, 0)) == -1
    assert Angel(390, 0).compare(Angel(30, 0)) == 0


def test_bad_minutes():
    with pytest.raises(ValueError):
        Angel(10, 60)


def test_read(monkeypatch):
    answers = iter(["45", "15"])
    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(answers),
    )

    assert Angel.read() == (45, 15)


def test_display(capsys):
    Angel(45, 15).display()
    assert "45° 15′" in capsys.readouterr().out
