import copy
import csv
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
        self.temp = copy.copy(self.people)

    #迭代器
    # def __iter__(self):
    #     return self

    #增加功能
    def append(self,obj):
        self.people.append(obj)

    #删除功能
    def pop(self,index):
        self.people.pop(index)

    #查找功能
    def query_list(self):
        return self.people

    def next(self):
        id_=copy.copy(self.current_id)
        while True:
            size = len(self.temp)
            if size == 0:
                raise StopIteration
            id_ = (id_+(self.step-1)) % len(self.temp)
            ret = self.temp.pop(id_)
            yield ret

    def reset(self):
        self.current_id = self.start - 1
        self.temp = copy.copy(self.people)


class ReadFile(object):
    #读文件类
    def __init__(self,path_name):
        self.path_name = path_name
        self.txt_file = None
        self.csv_file = None

    #关闭文件
    def close_file(self,file):
        file.close()

    #读取txt文件
    def open_txt(self):
        self.txt_file = open(self.path_name,"r")
        f = self.txt_file.readlines()
        return f

    #读取csv文件
    def open_csv(self):
        self.csv_file = open(self.path_name,"r")
        reader = csv.reader(self.csv_file)
        return reader

if __name__ == '__main__':  
    jos = JosephusRing(1,2)
    # jos.append(Person("Lisa", 13))
    # jos.append(Person("Aha", 15))
    # jos.append(Person("Bob", 12))
    # jos.append(Person("Cindy", 15))
    # jos.append(Person("Joan", 14))
    # jos.append(Person("Rose", 19))

    # 处理读出的txt文件数据，读出的txt文件以每一行为一个字符串元素存储在列表里
    # f = ReadFile("C:/Users/王丹丹/Desktop/python/person.txt")
    # data = f.open_txt()
    # for i in data:
    #     temp = i.strip('\n') 
    #     name = temp[ : temp.index(',')]
    #     age = temp[temp.index(',')+1 : ]
    #     jos.append(Person(name,age))
    # #关闭文件
    # f.close_file(f.txt_file)

    #处理读出的csv文件数据，读出的csv文件的每一行为一个列表，姓名与年龄为每个列表里的两个元素
    f = ReadFile("C:/Users/王丹丹/Desktop/python/person.CSV")
    data = f.open_csv()
    for i in data:
        name = i[0]
        age = i[1]
        jos.append(Person(name,age))
    #关闭文件
    f.close_file(f.csv_file)    

    jos.reset()
    lengh = len(jos.people)
    peo = jos.next()
    for i in range(lengh):    
        print("淘汰者名字是:",peo.__next__().name)



    



