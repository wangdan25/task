from josephus.joseph import joseph as jos
from josephus.domain import person as ps
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
