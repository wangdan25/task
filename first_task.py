#生成两个随机数
import random
a=random.randint(1,100)
b=random.randint(1,100)
print("a的值是%d,b的值是%d"%(a,b))
#交换两个随机数大小
a,b=b,a
print("交换数值后a的值是%d,b的值是%d"%(a,b))
#判断a是否是素数
if a<2:
    print("a不是一个素数")
else:
    for i in range(2,100):
        if a%i==0:
            print("a不是一个素数")
            break
    else:
        print("a是一个素数")
#把摄氏度变为华氏度
c=float(input("请输入一个摄氏度"))
d=c*9/5+32
print("转化后的为%.2F华氏度"%d)
#删除列表里的重复项
lst=["电子科大","python",23,"python",23]
print(lst)
print(list(set(lst)))





