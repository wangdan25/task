from Joseph.domain.person import Person
def test_person_init():
    person = Person(name="lily", age=11)
    assert person.name == "lily"
    assert person.age == 11

def test_person_comparison():
    person1 = Person("ella", 12)
    person2 = Person("ella", 12)
    assert person1 == person2