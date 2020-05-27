from josephus.adapter import file_reader as rd
from josephus.joseph import joseph as jos

class Interface():
    
    def check_start_value(self, start):
        if start < 0:
            raise ValueError

    def check_step_value(self,step):
        if step < 1:
            raise ValueError

    def read_data(self, path):
        file_ = path.split(".")
        if file_[1] == "txt":
            reader = rd.TxtReader(path)
        elif file_[1] == "csv":
            reader = rd.CsvReader(path)
        else:
            raise FileNotFoundError
        return reader.read_data()

    def create_joseph(self, reader, start, step):
        obj = jos.JosephusRing(reader)
        obj.start = start
        obj.step = step
        return obj
                