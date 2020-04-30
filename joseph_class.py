import copy
import csv
import os
import zipfile

class Person(object):
    def __init__(self, name, age):
        self.name = name
        if age<0:
            raise ValueError("The age has to be greater than 0")
        self.age = age

#约瑟夫环是一个容器，容器的功能有增删查改
class JosephusRing(object):
    def __init__(self, reader=None):
        self.start = 0
        self.step = 0
        self._people = []
        if reader:
            for each in reader:
                self._people.append(each)

    def append(self, obj):
        self._people.append(obj)

    def pop(self, index):
        self._people.pop(index)

    def query_list(self):
        return self._people

    def next(self):
        id_ = self.start - 1
        temp = copy.copy(self._people)
        while len(temp):
            id_ = (id_ + (self.step-1)) % len(temp)
            ret = temp.pop(id_)
            yield ret

#定义一个接口对继承类进行约束
class Reader(object):
    def read_data(self):
        raise NotImplementedError

class TxtReader(Reader):
    def __init__(self, path):
        self.path = path

    def read_data(self):
        reader = []
        with open(self.path, "r") as txt_file:
            for line in txt_file:
                data = line.strip().split(",")
                name = data[0]
                age = int(data[1])
                reader.append(Person(name, age))
            return reader

class CsvReader(Reader):
    def __init__(self, path):
        self.path = path 

    def read_data(self,):
        reader = []
        with open(self.path, "r") as csv_file:
            data = csv.reader(csv_file)
            for line in data:       
                name = line[0]
                age = int(line[1])
                reader.append(Person(name, age))
            return reader

class TxtFromZipReader(TxtReader):
    def __init__(self, path, file_name):
        with zipfile.ZipFile(path) as zip_file:
            self.file_path = zip_file.extract(file_name)  
            
    def read_data(self):
        TxtReader.__init__(self, self.file_path)
        return TxtReader.read_data(self)

class CsvFromZipReader(CsvReader):
    def __init__(self, path, file_name):
        with zipfile.ZipFile(path) as zip_file:
            self.file_path = zip_file.extract(file_name)  
            
    def read_data(self):
        TxtReader.__init__(self, self.file_path)
        return CsvReader.read_data(self)  

if __name__ == '__main__':  
    # jos.append(Person("Lisa", 13))
    # jos.append(Person("Aha", 15))
    # jos.append(Person("Bob", 12))
    # jos.append(Person("Cindy", 15))
    # jos.append(Person("Joan", 14))
    # jos.append(Person("Rose", 19))

    data = TxtFromZipReader("person.zip","person.txt")
    reader = data.read_data()
    ring = JosephusRing(reader)
    ring.start = 1
    ring.step = 2
    length = len(ring.query_list())
    generator_peple = ring.next()
    for i in range(length):   
        peo = generator_peple.__next__()
        print("淘汰者名字是:{},年龄是:{}".format(peo.name,peo.age))


    



