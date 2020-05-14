from Joseph.joseph import joseph as josephus
from Joseph.domain.person import Person
import pytest


person1 = Person("lily", 12)
person2 = Person("lisa", 11)

def test_josephus_init():
    jos = josephus.JosephusRing()
    assert jos.start == 0
    assert jos.step == 0
    assert jos._people == []

def test_josephus_append():
    jos = josephus.JosephusRing()
    jos._people.append(person1)
    assert jos._people == [person1]

def test_joseph_pop():
    jos = josephus.JosephusRing()
    jos._people = [person1, person2]
    jos.pop(0)
    assert jos._people == [person2]

def test_josephus_query_list():
    jos = josephus.JosephusRing()
    jos._people = [person1, person2]
    person = jos.query_list()
    assert person == [person1, person2]

def test_josephus_next():
    jos = josephus.JosephusRing()
    jos.start = 1
    jos.step = 2
    jos._people = [person1, person2]
    generator_people = jos.next()
    result1 = generator_people.__next__()
    result2 = generator_people.__next__()
    assert result1 == person2
    assert result2 ==person1


