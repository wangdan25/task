import unittest
from unittest.mock import MagicMock

from josephus.joseph.joseph import JosephusRing
from josephus.domain.person import Person
from josephus.adapter.file_reader import TxtReader
from josephus.adapter.file_reader import CsvReader

class TestJosephWithReader(unittest.TestCase):
    def setUp(self):
        mock = MagicMock()
        mock.__iter__.return_value = [Person("Lisa", 13), Person("Aha", 15)]
        self.ring = JosephusRing(mock)

    def test_josephus_init(self):
        assert self.ring.start == 0
        assert self.ring.step == 0
        assert self.ring.people == [Person("Lisa", 13), Person("Aha", 15)]

    def test_josephus_append(self):
        self.ring.people.append(Person("jeona", 12))
        assert self.ring.people == [Person("Lisa", 13), Person("Aha", 15),Person("jeona", 12)]

    def test_joseph_pop_(self):
        self.ring.pop(0)
        assert self.ring.people == [Person("Aha", 15)]

    def test_josephus_query_list(self):
        person = self.ring.query_list()
        assert person == [Person("Lisa", 13), Person("Aha", 15)]

    def test_josephus_next(self):
        self.ring.start = 1
        self.ring.step = 2
        result1 = next(self.ring)
        result2 = next(self.ring)
        assert result1 == Person("Aha", 15)
        assert result2 == Person("Lisa", 13)


        



    



