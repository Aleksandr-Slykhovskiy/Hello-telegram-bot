#!/usr/bin/env python3
"""
Тесты для Telegram бота
"""

import sys
import os

# Добавляем текущую директорию в путь чтобы импортировать bot
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from bot import click_counters


def test_click_counters_initialized():
    """Тест: счетчики инициализированы нулями"""
    expected = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0}
    assert click_counters == expected, f"Ожидалось {expected}, получено {click_counters}"


def test_click_counter_structure():
    """Тест: структура счетчиков корректна"""
    assert isinstance(click_counters, dict), "click_counters должен быть словарем"
    assert len(click_counters) == 5, "Должно быть 5 счетчиков для кнопок 1-5"

    for key in ["1", "2", "3", "4", "5"]:
        assert key in click_counters, f"Ключ {key} отсутствует в счетчиках"
        assert isinstance(click_counters[key], int), f"Счетчик для {key} должен быть числом"


def test_click_counters_can_increment():
    """Тест: счетчики можно увеличивать"""
    # Сохраняем исходные значения
    original_values = click_counters.copy()

    # Увеличиваем счетчики
    click_counters["1"] += 1
    click_counters["3"] += 5

    # Проверяем что значения изменились
    assert click_counters["1"] == original_values["1"] + 1
    assert click_counters["3"] == original_values["3"] + 5

    # Возвращаем исходные значения
    click_counters.update(original_values)


if __name__ == "__main__":
    test_click_counters_initialized()
    test_click_counter_structure()
    test_click_counters_can_increment()
    print("✅ Все тесты прошли успешно!")