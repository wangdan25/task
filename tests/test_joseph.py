from Joseph.joseph import joseph as josephus
from Joseph.domain.person import Person

def person_list():
    return [Person("lily", 12), Person("lisa", 11)]

def test_josephus_init():
    jos = josephus.JosephusRing()
    assert jos.start == 0
    assert jos.step == 0
    assert jos.person == []

def test_josephus_append():
    jos = josephus.JosephusRing()
    jos._people.append(person_list()[0])
    assert jos._people == [person_list()[0]]

def test_joseph_pop():
    jos = josephus.JosephusRing()
    jos._people = [person_list()[0], person_list()[1]]
    jos.pop(0)
    assert jos._people == [person_list()[1]]

def test_josephus_query_list():
    jos = josephus.JosephusRing()
    jos._people = [person_list()[0], person_list()[1]]
    person = jos.requery_list()
    assert person == [person_list()[0], person_list()[1]]

def test_josephus_next():
    jos = josephus.JosephusRing()
    jos.start = 0
    jos.step = 1
    jos._people = [person_list()[0], person_list()[1]]
    assert jos.next() == person_list()[1]
    assert jos.next() == person_list()[0]


