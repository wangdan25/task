import copy
from josephus.domain import person as ps
from typing import List,Iterator
#约瑟夫环是一个容器，容器的功能有增删查改
class JosephusRing(object):
    def __init__(self, reader: List[ps.Person]=None):
        self.start = 0
        self.step = 0
        self.people = []
        if reader:
            for each in reader:
                self.people.append(each)
    
    def __len__(self):
        return len(self.people)

    def append(self, obj: ps.Person):
        self.people.append(obj)

    def pop(self, index):
        self.people.pop(index)

    def query_list(self) -> List[ps.Person]:
        return self.people

    def __iter__(self):
        return self

    def __next__(self) -> Iterator[ps.Person]:
        if not self.people:
            raise StopIteration
        id_ = self.start - 1
        id_ = (id_ + (self.step-1)) % len(self.people)
        ret = self.people.pop(id_)
        return ret

#定义一个接口对继承类进行约束
class Reader(object):
    def read_data(self) -> List[ps.Person]:
        raise NotImplementedError