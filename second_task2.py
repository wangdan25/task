def josephus_problem(delete_k,n):
    #生成一个n个人的列表
    people=list(range(1,n+1))
    if delete_k==1:
        return n
    index=0 
    delete_people=list()
    while len(people)!=1:
        #被淘汰者索引
        index=(index+(delete_k-1))%len(people)
        delete_people.append(people[index])
        del people[index]
    survive_people=people[0]
    return (delete_people,survive_people)

try:
    k=int(input("输入循环的号码"))
    n=int(input("输入总的人数"))
    if (k<=0)or(n<=0):
        raise Exception("输入的值必须是正整数!")
except Exception as e:
    print(e)
else:
    print("被淘汰的人和幸存者分别是：",josephus_problem(k,n))




            

           

