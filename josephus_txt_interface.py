from josephus.joseph import joseph as jos
from josephus.domain import person as ps
from josephus.adapter import create_ui_reader as rd

print("******************************约瑟夫环游戏***********************************")
file_name= input("请输入文件路径:")
ui_reader = rd.CreateUiReader(file_name)
reader = ui_reader.create_ui_reader()
print("约瑟夫环的人有：")
length = len(reader)
for i in range(length):
    print("初始的人的名字是{},年龄是{}".format(reader[i].name,reader[i].age))
ring = jos.JosephusRing(reader)
try:
    ring.start = int(input("输入约瑟夫起始值:"))
    ring.step = int(input("输入约瑟夫步进值:"))
except:
    print("起始值和步进值必须是正整数")
    raise Exception

length = len(ring.query_list())
generator_people = ring.next() 
for i in range(length):   
    peo = generator_people.__next__()
    print("淘汰的人的名字是{},年龄是{}".format(peo.name, peo.age))
print("**********************************游戏结束*************************************")


        



    



