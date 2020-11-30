import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Тесты для 'name_function.py'."""

    def test_first_last_name(self):
        """Имена вида 'Janis Joplin' работают правильно?"""
        formated_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formated_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """Имена из трёх компонентов работают правильно?"""
        formated_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formated_name, 'Wolfgang Amadeus Mozart')


unittest.main()