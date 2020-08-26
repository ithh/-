
def adder(x):
    '递归练习'
    def wrapper(y):   
        return x + y   
    return wrapper
adder5 = adder(5)
print(adder5(6))
print(adder5(adder5(6)))



def test(a, b, *args, **kwargs):
    '''
    对python参数进一步了解
    *args表示任何多个无名参数，它是一个tuple；**kwargs表示关键字参数，它是一个dict。
    并且同时使用*args和**kwargs时，必须*args参数列要在**kwargs前
    '''
    print(a)
    print(b)
    print(args)
    print(kwargs)
# test(11,22,33,44,55,66,77, a=1, b=2)
# test(11,22,33,44,55,66,77, x=1, y=2)

def kw_dict(**kwargs):
    '利用关键字参数创建字典，dict()方法也可以做到'
    return kwargs
# print (kw_dict(a=1,b=2,c=3))



def func(s, i, j):
    '倒序输出列表'
    if i < j:
        func(s, i + 1, j - 1)
        s[i],s[j] = s[j], s[i]
def main():
    a = [10, 6, 23, -90, 0, 3]
    func(a, 0, len(a)-1)
    for i in range(6):
        print (a[i])
# main()


