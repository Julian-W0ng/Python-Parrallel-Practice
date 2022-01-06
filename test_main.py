from unittest import TestCase
from main import PathFinder
import wikipediaapi


class Test(TestCase):
    def test_pathfinder_base(self):
        path = PathFinder.find_path('Avril Lavigne', 'Timmins')
        print(path)
        self.assert_(len(path) == 3)


