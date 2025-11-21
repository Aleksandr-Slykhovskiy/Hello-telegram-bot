import sqlite3
import os
from datetime import datetime


class ClickCounterDB:
    def __init__(self, db_path="click_counter.db"):
        self.db_path = db_path
        self.init_db()

    def init_db(self):
        """Инициализация базы данных и таблицы"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Создаём таблицу
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS click_counter (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                counter_value INTEGER DEFAULT 0,
                last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        # Инициализируем счётчик, если его нет
        cursor.execute('INSERT OR IGNORE INTO click_counter (id, counter_value) VALUES (1, 0)')

        conn.commit()
        conn.close()
        print(f"База данных создана: {self.db_path}")

    def get_count(self):
        """Получить текущее значение счётчика"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('SELECT counter_value FROM click_counter WHERE id = 1')
        result = cursor.fetchone()

        conn.close()
        return result[0] if result else 0

    def increment_count(self):
        """Увеличить счётчик на 1"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Исправляем для Python 3.12+ - используем строку вместо datetime
        cursor.execute(
            'UPDATE click_counter SET counter_value = counter_value + 1, last_updated = datetime("now") WHERE id = 1'
        )

        conn.commit()
        conn.close()

        return self.get_count()


# Тестируем базу
if __name__ == "__main__":
    db = ClickCounterDB()
    print(f"Текущее значение счётчика: {db.get_count()}")
    print(f"После увеличения: {db.increment_count()}")