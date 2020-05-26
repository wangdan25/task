import unittest
from unittest import mock

from josephus.joseph.joseph import JosephusRing
from josephus.domain.person import Person
from josephus.adapter.file_reader import TxtReader
from josephus.adapter.file_reader import CsvReader


def test_josephus_init_with_txt_reader():
    TxtReader.read_data = mock.Mock(return_value=[Person("Lisa", 13), Person("Aha", 15)])
    reader = TxtReader.read_data()
    jos = JosephusRing(reader)
    assert jos.start == 0
    assert jos.step == 0
    assert jos.people == [Person("Lisa", 13), Person("Aha", 15)]

def test_josephus_append_with_txt_reader():
    TxtReader.read_data = mock.Mock(return_value=[Person("Lisa", 13), Person("Aha", 15)])
    reader = TxtReader.read_data()
    jos = JosephusRing(reader)
    jos.people.append(Person("jeona", 12))
    assert jos.people == [Person("Lisa", 13), Person("Aha", 15),Person("jeona", 12)]

def test_joseph_pop_with_txt_reader():
    TxtReader.read_data = mock.Mock(return_value=[Person("Lisa", 13), Person("Aha", 15)])
    reader = TxtReader.read_data()
    jos = JosephusRing(reader)
    jos.pop(0)
    assert jos.people == [Person("Aha", 15)]


def test_josephus_query_list_with_txt_reader():
    TxtReader.read_data = mock.Mock(return_value=[Person("Lisa", 13), Person("Aha", 15)])
    reader = TxtReader.read_data()
    jos = JosephusRing(reader)
    person = jos.query_list()
    assert person == [Person("Lisa", 13), Person("Aha", 15)]

def test_josephus_next_with_txt_reader():
    TxtReader.read_data = mock.Mock(return_value=[Person("Lisa", 13), Person("Aha", 15)])
    reader = TxtReader.read_data()
    jos = JosephusRing(reader)
    jos.start = 1
    jos.step = 2
    result1 = next(jos)
    result2 = next(jos)
    assert result1 == Person("Aha", 15)
    assert result2 == Person("Lisa", 13)


        



    



