#!/usr/bin/env python3
"""
Тесты для Telegram бота с базой данных
"""

import sys
import os
import pytest
import tempfile

# Добавляем текущую директорию в путь чтобы импортировать модули
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database import ClickCounterDB


class TestClickCounterDB:
    """Тесты для базы данных счетчика кликов"""

    def setup_method(self):
        """Создаем временную базу для тестов"""
        self.temp_db = tempfile.NamedTemporaryFile(delete=False, suffix='.db')
        self.db_path = self.temp_db.name
        self.db = ClickCounterDB(db_path=self.db_path)

    def teardown_method(self):
        """Удаляем временную базу после тестов"""
        if os.path.exists(self.db_path):
            os.remove(self.db_path)

    def test_db_initialization(self):
        """Тест: база данных инициализируется с нулевым значением"""
        count = self.db.get_count()
        assert count == 0, f"Ожидалось 0, получено {count}"

    def test_increment_count(self):
        """Тест: счетчик увеличивается корректно"""
        # Первое увеличение
        count1 = self.db.increment_count()
        assert count1 == 1, f"Ожидалось 1, получено {count1}"

        # Второе увеличение
        count2 = self.db.increment_count()
        assert count2 == 2, f"Ожидалось 2, получено {count2}"

    def test_get_count(self):
        """Тест: получение значения счетчика"""
        # До увеличения
        initial_count = self.db.get_count()
        assert initial_count == 0

        # После увеличения
        self.db.increment_count()
        new_count = self.db.get_count()
        assert new_count == 1


def test_database_file_created():
    """Тест: файл базы данных создается"""
    with tempfile.NamedTemporaryFile(delete=False, suffix='.db') as temp_db:
        db_path = temp_db.name

    try:
        # Создаем базу
        db = ClickCounterDB(db_path=db_path)

        # Проверяем что файл создан
        assert os.path.exists(db_path), "Файл базы данных не создан"

        # Проверяем что счетчик работает
        count = db.get_count()
        assert count == 0

    finally:
        # Удаляем временный файл
        if os.path.exists(db_path):
            os.remove(db_path)


if __name__ == "__main__":
    # Запускаем тесты вручную
    test_db = TestClickCounterDB()

    test_db.setup_method()
    try:
        test_db.test_db_initialization()
        test_db.test_increment_count()
        test_db.test_get_count()
        print("✅ Все тесты базы данных прошли успешно!")
    finally:
        test_db.teardown_method()

    test_database_file_created()
    print("✅ Все тесты прошли успешно!")