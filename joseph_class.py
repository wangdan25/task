import copy
import csv
import os
import zipfile

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

#约瑟夫环是一个容器，容器的功能有增删查改
class JosephusRing(object):
    def __init__(self):
        self.start = 0
        self.step = 0
        self.current_id = self.start - 1
        self.__people = []
        self.temp = copy.copy(self.__people)

    def append(self, obj):
        self.__people.append(obj)

    def pop(self, index):
        self.__people.pop(index)

    def query_list(self):
        return self.__people
    
    def ring_lengh(self):
        return len(self.__people)

    def next(self):
        id_=copy.copy(self.current_id)
        while True:
            size = len(self.temp)
            if size == 0:
                raise StopIteration
            id_ = (id_ + (self.step-1)) % len(self.temp)
            ret = self.temp.pop(id_)
            yield ret

    def reset(self):
        self.current_id = self.start - 1
        self.temp = copy.copy(self.__people)
    
    @classmethod
    def creat_from_csv(cls, path):
        obj = cls()
        with open(path,"r") as csv_file:
            reader = csv.reader(csv_file)
            for line in reader:
                obj.append(Person(name=line[0], age=line[1]))
            return obj

    @classmethod
    def creat_from_txt(cls, path):
        obj = cls()
        with open(path,"r") as txt_file:
            for line in txt_file:
                temp = line.strip() 
                name = temp[ : temp.index(',')]
                age = temp[temp.index(',') + 1: ]
                obj.append(Person(name,age))
            return obj
    
    @classmethod
    def creat_from_zip(cls, path):
        # obj_ = cls()
        with zipfile.ZipFile(path) as zip_file:
            file_list = zip_file.namelist()
            choose_file = input("选择文件:{}".format(file_list))
            file_path = zip_file.extract(choose_file)
            file_type = os.path.splitext(file_path)[1]
            if file_type == ".txt":
                return cls.creat_from_txt(file_path)
            if file_type == ".CSV":
                return cls.creat_from_csv(file_path)
            
if __name__ == '__main__':  
    # jos.append(Person("Lisa", 13))
    # jos.append(Person("Aha", 15))
    # jos.append(Person("Bob", 12))
    # jos.append(Person("Cindy", 15))
    # jos.append(Person("Joan", 14))
    # jos.append(Person("Rose", 19))
   
    zip = JosephusRing.creat_from_zip("person.zip")
    zip.start = 1
    zip.step = 2
    zip.reset()
    lengh = zip.ring_lengh()
    generator_peple = zip.next()
    for i in range(lengh):   
        peo = generator_peple.__next__()
        print("淘汰者名字是:{},年龄是:{}".format(peo.name,peo.age))



    



