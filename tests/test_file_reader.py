from Joseph.file_reader import file_reader
from Joseph.domain.person import Person

def test_txt_reader_init():
    txt_reader = file_reader.TxtReader("person.txt")
    assert txt_reader.path == "person.txt"

def test_txt_reader_read_data():
    txt_reader = file_reader.TxtReader("person.txt")
    result = txt_reader.read_data()
    assert result == [
        Person("Lisa", 13),
        Person("Aha", 15),
        Person("Bob", 12),
        Person("Cindy", 15),
        Person("Joan", 14),
        Person("Rose", 19)
    ]

def test_csv_reader_init():
    csv_reader = file_reader.CsvReader("person.CSV")
    assert csv_reader.path == "person.CSV"

def test_csv_file_reader_read_data():
    csv_reader = file_reader.CsvReader("person.CSV")
    result = csv_reader.read_data()
    assert result == [
        Person("Lisa", 13),
        Person("Aha", 15),
        Person("Bob", 12),
        Person("Cindy", 15),
        Person("Joan", 14),
        Person("Rose", 19)
    ]
