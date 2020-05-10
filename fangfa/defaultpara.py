#conding=utf-8
'''
# def student(age,naem,sex,guoji="中国"):
#     return age,naem,sex,guoji
#
# print("任伟","")

def boy(profile,*mytuple):
    out_put = ""

    for parameter in mytuple:
        if not out_put:
            out_put = out_put + parameter
        else:
            out_put = out_put + "," + parameter
    return profile ,":",out_put

print (boy('age',"任伟","男","山西运城人","28岁"))

def add(x,**key):
    total = x
    for arg,value in key.items():
        print("hei,加了",arg)
        total += value
    return total
print(add(10,a=11,b=12,c=13))

def add(x,key):
# 不定长函数，用于页面接口新增参数时不需要改变方法了
    total = x
    for arg,value in key.items():
        print("hei,加了",arg)
        total += value
    return total
input_dic={"x":11,"y":12}
print(add(10,input_dic))

# lambda
add = lambda  x,y : x+y
print(add(1,2))

'''
# map,注意python3中map()返回iterators类型，不再是list类型。进行list转换即可
def sqr(x):
    return x ** 2
a = [4,5,8]

print(list(map(sqr,a)))
