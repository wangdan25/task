from josephus.joseph import joseph as jos
from josephus.domain import person as ps
from josephus.adapter.interface import Interface

class TxtInterface(Interface):

    def set_start_value(self):
        start = int(input("请输入步进值："))
        try:
            self.check_start_value(start)
        except ValueError:
            print("起始值应大于0！")
        return start

    def set_step_value(self):
        step = int(input("请输入步进值："))
        try:
            self.check_step_value(step)
        except ValueError:
            print("步进大于1！")
        return step

    def create_reader(self):
        try:
            path = input("输入文件路径：")
        except FileNotFoundError:
            print("文件路径错误")
        reader = self.read_data(path)
        return reader

    def show_original_data(self, reader):
        print("原始数据是：")
        for each in reader:
            print("约瑟夫环里的人是{},年龄是{}".format(each.name, each.age))

    def show_result(self, reader):
        start = self.set_start_value()
        step = self.set_step_value()
        ring = self.create_joseph(reader, start, step)
        print("结果是：")
        for each in ring:
            print("被淘汰的人是{},年龄是{}".format(each.name, str(each.age)))


    





        



    



