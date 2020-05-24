from josephus.joseph import joseph as jos
from josephus.domain import person as ps
from josephus.adapter import read_data as rd

def set_josephus_start():
    start = int(input("请输入步进值："))
    if start < 0:
        raise ValueError("起始值是正整数！")
    return start

def set_josephus_step():
    start = int(input("请输入步进值："))
    if start < 1:
        raise ValueError("步进是正整数！")
    return start

def create_reader():
    try:
        path = input("输入文件路径：")
    except:
        raise FileNotFoundError("路径错误")
    reader = rd.read_data(path)
    return reader

def show_original_data(reader):
    print("原始数据是：")
    for each in reader:
        print("约瑟夫环里的人是{},年龄是{}".format(each.name, each.age))

def show_result(reader):
    print("结果是：")
    ring = jos.JosephusRing(reader)
    for each in ring:
        print("被淘汰的人是{},年龄是{}".format(each.name, str(each.age)))

if __name__ == '__main__':
    print("******************************约瑟夫环游戏***********************************")
    set_josephus_start()
    set_josephus_step()
    reader = create_reader()
    show_original_data(reader)
    show_result(reader)
    print("********************************游戏结束*************************************")




        



    



