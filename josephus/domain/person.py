class Person(object):
    def __init__(self, name: str = None, age: int = 0):
        self.name = name
        if age < 0:
            self.age = 0
        else:
            self.age = age 
            
    # 判断两个person对象相等的条件
    def __eq__(self, obj):
        return self.name == obj.name and self.age == obj.age