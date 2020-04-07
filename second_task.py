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

print(josephus_problem(4,10))
print(josephus_problem(3,6))



            

           

