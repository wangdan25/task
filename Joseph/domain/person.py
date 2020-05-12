class Person(object):
    def __init__(self, name: str, age: int):
        self.name = name
        if age<0:
            raise ValueError("The age has to be greater than 0")
        self.age = age