import unittest
from josephus.domain.person import Person


class TestPerson(unittest.TestCase):
    def test_person_init(self):
        person = Person(name="lily", age=11)
        assert person.name == "lily"
        assert person.age == 11

    def test_person_init_without_parameter(self):
        person = Person()
        assert person.name == None
        assert person.age == 0

    def test_person_the_value_of_age_less_than_zero(self):
        person = Person(age=-1)
        assert person.name == None
        assert person.age == 0

    def test_person_comparison(self):
        person1 = Person("ella", 12)
        person2 = Person("ella", 12)
        assert person1 == person2