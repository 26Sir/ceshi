#conding=utf-8

from selenium import webbrowser
'''
age = 18
sex = "F"
if sex == "F":
    print("这是一个女孩子")
    if age >= 16:
        print("马上就成年了")
    elif age <16:
        print("还早着呢")
elif sex == "M":
    print("这是男孩子")
else:
    print("你猜是什么")


companys = ["google","baidu","ali"]

for company in companys:
        print(company)
        if company == "google":
            print("国外大厂。走走走")
        elif company == "baidu":
            print("狗哥去了")
        else:
            print("狗哥最想去的公司")


for first_number in range(1,10):
    for second_number in range(1,first_number+1):
        print(first_number,"*",second_number,"=",first_number*second_number,end="  ")
    print("\n")

wid = 1
while wid <=5:
    len = 1
    while len <= wid:
        print("*",end=" ")
        len+=1
    print("\n")
    wid+=1


age = 0
while age < 7:
    if age >2:
        print("上幼儿园吧")
        #break
    print("还小，才",age,"岁,不上学")
    age = age +1
'''

age = 0
while age < 7:
    age = age + 1
    if age - 1 < 2:
        print("还小，才",age,"岁,不上学")
        continue
    print(age,"岁上幼儿园吧")

'''
file_in = open("./yufa.py","r",encoding="utf-8")
count = file_in.read()
print(count)

def read_file(in_file):

    :param in_file:
    :return:

    try:
        file_in = open(in_file,"r",encoding="utf-8")
    except Exception as e:
        print(e)
    else:
        cout = file_in.read()
        print(cout)

read_file("./yufa.py")
'''
