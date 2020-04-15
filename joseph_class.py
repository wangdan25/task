class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

#约瑟夫环是一个容器，容器的功能有增删查改
class JosephusRing(object):
    def __init__(self, start, step):
        self.start = start
        self.step = step
        self.current_id = self.start - 1
        self.people = []
        self.temp = self.people

    #迭代器
    def __iter__(self):
        return self

    #增加功能
    def append(self,obj):
        self.people.append(obj)

    #删除功能
    def pop(self,index):
        self.people.pop(index)

    #查找功能
    def query_list(self):
        return self.people

    def __next__(self):
        size = len(self.temp)
        if size == 0:
            raise StopIteration
        self.current_id = (self.current_id+(self.step-1)) % len(self.people)
        ret = self.temp.pop(self.current_id)
        return ret

    def reset(self):
        self.current_id = self.start - 1
        self.temp = self.people

if __name__ == '__main__':  
    jos = JosephusRing(1,2)
    jos.append(Person("Lisa", 13))
    jos.append(Person("Aha", 15))
    jos.append(Person("Bob", 12))
    jos.append(Person("Cindy", 15))
    jos.append(Person("Joan", 14))
    jos.append(Person("Rose", 19))
    jos.reset()
    lengh=len(jos.people)
    for i in jos:
        print("淘汰者名字是:{},年龄是:{}".format(i.name,i.age))

    



