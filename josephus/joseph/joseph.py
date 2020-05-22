import copy
from josephus.domain import person as ps
from typing import List,Iterator
#约瑟夫环是一个容器，容器的功能有增删查改
class JosephusRing(object):
    def __init__(self, reader: List[ps.Person]=None):
        self.start = 0
        self.step = 0
        self._people = []
        if reader:
            for each in reader:
                self._people.append(each)

    def append(self, obj: ps.Person):
        self._people.append(obj)

    def pop(self, index):
        self._people.pop(index)

    def query_list(self) -> List[ps.Person]:
        return self._people

    def next(self) -> Iterator[ps.Person]:
        id_ = self.start - 1
        temp = copy.copy(self._people)
        while len(temp):
            id_ = (id_ + (self.step-1)) % len(temp)
            ret = temp.pop(id_)
            yield ret

#定义一个接口对继承类进行约束
class Reader(object):
    def read_data(self) -> List[ps.Person]:
        raise NotImplementedError