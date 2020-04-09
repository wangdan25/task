class josephus(object):
    def lastRemaining_solution(self,start_value,step,name):
        #新建一个保存被淘汰的人的列表
        delete_name=list()

        for i in range(0,len(name)-1):
            #被淘汰者索引
            start_value=(start_value+(step-1))%len(name)
            delete_name.append(name[start_value])
            name.pop(start_value)
        final_name=name[0]

        return (delete_name,final_name)

name=["Lili","Lisa","Aha", "Bob", "Cindy","Marry","Joan","Rose"]
jos=josephus()
print("被淘汰的的人和被留下的人分别是：",jos.lastRemaining_solution(2,2,name))




            

           

