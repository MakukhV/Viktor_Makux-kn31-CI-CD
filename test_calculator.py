import unittest
from calculator import add, subtract  # Переконайтеся, що цей імпорт відповідає правильному модулю
# Якщо вам потрібно тестувати calculator2.py також, імпортуйте спеціально і перейменуйте функції, щоб уникнути конфлікту.

class TestCalculator(unittest.TestCase):
    def test_add(self):
        """Перевіряє, чи працює функція додавання."""
        self.assertEqual(add(3, 4), 7)

    def test_subtract(self):
        """Перевіряє, чи працює функція віднімання."""
        self.assertEqual(subtract(5, 2), 3)

# Якщо є тести для calculator2, визначте інший клас TestCase тут або в іншому файлі.

if __name__ == '__main__':  # Виправлена умова перевірки для запуску unittest
    unittest.main()
