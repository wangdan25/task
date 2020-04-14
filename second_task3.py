#两个对象：环和人

#对象1：环
class circular(object):
    def __init__(self,start,step,length):
        self.start=start
        self.step=step
        self.length=length
        self.out=list()
    # def creat_sequence(self):
    #     self.sequence=list(range(0,self.length))
    def out_num(self):
        self.sequence=list(range(0,self.length))
        for i in range(0,self.length):
            #被淘汰索引
            self.start=(self.start+(self.step-1))%len(self.sequence)
            self.out.append(self.sequence[self.start])
            self.sequence.pop(self.start)  
        return self.out    

#对象2：人
class humans(object):
    def __init__(self,people,show_order,length):
        self.people=people
        self.show_order=show_order
        self.length=length
    def show_people(self):
        for i in range(self.length):
            #利用字典的键输出名字和年龄
            self.index=self.show_order[i]
            print("被淘汰的人的名字和年龄是：",self.people[self.index])
            
people={0:["Lili",12],1:["Lisa",13],2:["Aha",15], 3:["Bob",12], 4:["Cindy",15],5:["Marry",17],6:["Joan",14],7:["Rose",19]}
length=len(people)
cir=circular(1,2,length)
show_order=cir.out_num()
peo=humans(people,show_order,length)
peo.show_people()




            

           

