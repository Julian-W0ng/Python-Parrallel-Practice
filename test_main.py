from unittest import TestCase
from main import find_path
import wikipediaapi


class Test(TestCase):
    def test_find_path_base(self):
        wiki = wikipediaapi.Wikipedia('en')
        path = find_path('Avril Lavigne', 'Avril Lavigne', wiki)
        print(path)
        self.assert_(len(path) == 1)

    def test_find_path_two(self):
        wiki = wikipediaapi.Wikipedia('en')
        path = find_path('Avril Lavigne', 'Shania Twain', wiki)
        print(path)
        self.assert_(len(path) == 2)

