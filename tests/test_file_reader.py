from josephus.adapter import file_reader as reader
from josephus.domain.person import Person

def test_txt_reader_init():
    txt_reader = reader.TxtReader("person.txt")
    assert txt_reader.path == "person.txt"

def test_txt_reader_read_data():
    txt_reader = reader.TxtReader("person.txt")
    result = txt_reader.read_data()
    assert result[0].name == "Lisa"
    assert result[0].age == 13
    assert result[1].name == "Aha"
    assert result[1].age == 15
    assert result[2].name == "Bob"
    assert result[2].age == 12
    assert result[3].name == "Cindy"
    assert result[3].age == 15
    assert result[4].name == "Joan"
    assert result[4].age == 14
    assert result[5].name == "Rose"
    assert result[5].age == 19

def test_csv_reader_init():
    csv_reader = reader.CsvReader("person.CSV")
    assert csv_reader.path == "person.CSV"

def test_csv_file_reader_read_data():
    csv_reader = reader.CsvReader("person.CSV")
    result = csv_reader.read_data()
    assert result[0].name == "Lisa"
    assert result[0].age == 13
    assert result[1].name == "Aha"
    assert result[1].age == 15
    assert result[2].name == "Bob"
    assert result[2].age == 12
    assert result[3].name == "Cindy"
    assert result[3].age == 15
    assert result[4].name == "Joan"
    assert result[4].age == 14
    assert result[5].name == "Rose"
    assert result[5].age == 19

