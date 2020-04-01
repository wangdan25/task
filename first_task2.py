def exchange_value():
    #交换两个数的值
    import random
    num1=random.randint(1,100)
    num2=random.randint(1,100)
    print(num1,num2)
    return num2,num1
print(exchange_value())

def is_prime(n):     
    #判断一个数是否是素数
    lower_bound=2
    upper_bound=int(n/2+1)
    if n <lower_bound:
        return False
    for i in range(lower_bound, upper_bound):
        if n % i == 0:
            return False
    return True
#验证
assert is_prime(5) == True
assert is_prime(11) == True
assert is_prime(8) == False

number=int(input("请输入一个整数："))
if is_prime(number)==True:    
    print("它是一个质数")
else:
    print("它不是一个质数")

def celsius_to_fahrenheit(celsius):              
    #把摄氏度变为华氏度
    fahrenheit=celsius*9/5+32
    return fahrenheit
#验证
cel=float(input("输入摄氏度"))
print(celsius_to_fahrenheit(cel))

def add_everynum(num):
    #将一个整数各位数相加
    sum=0
    str1=str(num)                #转化为字符串
    str2=str1.replace(".","0")   #把小数点用0代替
    for i in str2:
        sum=sum+int(i)
    return sum
#验证
assert add_everynum(32.1)==6
assert add_everynum(31)==4

num=input("请输入数字：")
print(add_everynum(num))

#删除列表里的重复项
def delete_duplicates():
    lst=["电子科大","python",23,"python",23]
    return list(set(lst))
print(delete_duplicates())








