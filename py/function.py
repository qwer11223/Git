def demo(a,b=0):
    '''
        函数描述信息
    '''
    print(a,b)

def varfunc(*tuple1):
    for i in tuple1:
        print(i)

def varfunc1(**dictionary):
    for key,value in dictionary.items():
        print(key,' : ',value)

list1 = [1,2,3]

dict1 = {'a':1,'b':2}

demo(1)
print(demo.__defaults__) #结果为一个元组,返回函数的默认值

print('----------\n')

varfunc(*list1)

print('----------\n')

varfunc1(**dict1)

print('--- 匿名函数 -------\n')


lambdafunc = lambda x:x**2

print(lambdafunc(2))