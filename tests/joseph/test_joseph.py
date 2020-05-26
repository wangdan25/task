import pytest

from josephus.joseph import joseph as josephus
from josephus.domain.person import Person


@pytest.fixture
def people_data():
    return [Person("lily", 12), Person("lisa", 11)]

def test_josephus_init():
    jos = josephus.JosephusRing()
    assert jos.start == 0
    assert jos.step == 0
    assert jos.people == []

def test_josephus_append(people_data):
    person1 = Person("lily", 12)
    jos = josephus.JosephusRing()
    jos.people.append(person1)
    assert jos.people == [person1]

def test_joseph_pop(people_data):
    jos = josephus.JosephusRing()
    jos.people = people_data
    jos.pop(0)
    assert jos.people == [Person("lisa", 11)]


def test_josephus_query_list(people_data):

    jos = josephus.JosephusRing()
    jos.people = people_data
    person = jos.query_list()
    assert person == people_data

def test_josephus_next(people_data):
    jos = josephus.JosephusRing()
    jos.start = 1
    jos.step = 2
    jos.people = people_data
    result1 = next(jos)
    result2 = next(jos)
    assert result1 == Person("lisa", 11)
    assert result2 == Person("lily", 12)


