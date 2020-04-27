import copy
import csv
import os
import zipfile

class Person(object):
    def __init__(self):
        self.name = None
        self.age = None

    @classmethod
    def creat_from_reader(cls, reader):
        obj = cls()
        obj.name = reader[0]
        obj.age = reader[1] 
        return obj

#约瑟夫环是一个容器，容器的功能有增删查改
class JosephusRing(object):
    def __init__(self, reader=None):
        self.start = 0
        self.step = 0
        self._people = []
        if reader:
            for each in reader:
                self._people.append(Person.creat_from_reader(each))

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

class ReadData(object):
    def __init__(self, path, file_name=None):
        self.path = path
        self.file_name = file_name
  
    def read_from_csv(self):
        data = []
        with open(self.path,"r") as csv_file:
            reader = csv.reader(csv_file)
            for i in reader:
                data.append(i)
        return data

    def read_from_txt(self):
        data = []
        with open(self.path,"r") as txt_file:
            for line in txt_file:
                temp = line.strip().split(",")
                data.append(temp)
            return data
    
    def read_from_zip(self):
        with zipfile.ZipFile(self.path) as zip_file:
            file_path = zip_file.extract(self.file_name)
            file_type = os.path.splitext(file_path)[1]
            if file_type == ".txt":
                self.path = file_path
                return self.read_from_txt()
            if file_type == ".CSV":
                self.path = file_path
                return self.read_from_csv()    
            
if __name__ == '__main__':  
    # jos.append(Person("Lisa", 13))
    # jos.append(Person("Aha", 15))
    # jos.append(Person("Bob", 12))
    # jos.append(Person("Cindy", 15))
    # jos.append(Person("Joan", 14))
    # jos.append(Person("Rose", 19))

    data = ReadData("person.zip", "person.txt")
    reader = data.read_from_zip()
    ring = JosephusRing(reader)
    ring.start = 1
    ring.step = 2
    length = len(ring.query_list())
    generator_peple = ring.next()
    for i in range(length):   
        peo = generator_peple.__next__()
        print("淘汰者名字是:{},年龄是:{}".format(peo.name,peo.age))



    



