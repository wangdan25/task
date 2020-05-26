import pytest
from josephus.adapter import file_reader as reader
from josephus.domain.person import Person

@pytest.fixture()
def people_data():
    return [
        Person("Lisa", 13), 
        Person("Aha", 15),
        Person("Bob", 12),
        Person("Cindy",15),
        Person("Joan", 14),
        Person("Rose", 19),
    ]

def test_txt_reader_init():
    txt_reader = reader.TxtReader("person.txt")
    assert txt_reader.path == "person.txt"

def test_txt_reader_read_data(people_data):
    txt_reader = reader.TxtReader("person.txt")
    result = txt_reader.read_data()
    assert result == people_data

def test_csv_reader_init():
    csv_reader = reader.CsvReader("person.CSV")
    assert csv_reader.path == "person.CSV"

def test_csv_file_reader_read_data(people_data):
    csv_reader = reader.CsvReader("person.CSV")
    result = csv_reader.read_data()
    assert result == people_data


