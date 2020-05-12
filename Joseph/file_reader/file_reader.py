from Joseph.joseph import joseph as jos
from Joseph.domain import person as ps
from typing import List

import csv
import os
import zipfile
class TxtReader(jos.Reader):
    def __init__(self, path: str):
        self.path = path

    def read_data(self) -> List[ps.Person]:
        reader = []
        with open(self.path, "r") as txt_file:
            for line in txt_file:
                data = line.strip().split(",")
                name = data[0]
                try:
                    age = int(data[1])
                except ValueError as e:
                    age = 0                
                reader.append(ps.Person(name, age))
            return reader

class CsvReader(jos.Reader):
    def __init__(self, path: str):
        self.path = path 

    def read_data(self) -> List[ps.Person]:
        reader = []
        with open(self.path, "r") as csv_file:
            data = csv.reader(csv_file)
            for line in data:       
                name = line[0]
                try:
                    age = int(line[1])
                except ValueError as e:
                    age = 0 
                reader.append(ps.Person(name, age))
            return reader

class TxtFromZipReader(TxtReader):
    def __init__(self, path: str, file_name: str):
        with zipfile.ZipFile(path) as zip_file:
            self.file_path = zip_file.extract(file_name)  
            
    def read_data(self) -> List[ps.Person]:
        super().__init__(self.file_path)
        return super().read_data()

class CsvFromZipReader(CsvReader):
    def __init__(self, path: str, file_name: str):
        with zipfile.ZipFile(path) as zip_file:
            self.file_path = zip_file.extract(file_name)  
            
    def read_data(self) -> List[ps.Person]:
        super().__init__(self.file_path)
        return super().read_data()  

if __name__ == '__main__':  
    # jos.append(Person("Lisa", 13))
    # jos.append(Person("Aha", 15))
    # jos.append(Person("Bob", 12))
    # jos.append(Person("Cindy", 15))
    # jos.append(Person("Joan", 14))
    # jos.append(Person("Rose", 19))

    data = TxtReader("person.txt")
    reader = data.read_data()
    ring = jos.JosephusRing(reader)
    ring.start = 1
    ring.step = 2
    length = len(ring.query_list())
    generator_people = ring.next()
    for i in range(length):   
        peo = generator_people.__next__()
        print("淘汰者名字是:{},年龄是:{}".format(peo.name,peo.age))
