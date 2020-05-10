from datetime import datetime

now = datetime.now()
print(now)

year = now.year
month = now.month
day = now.day
print(year,month,day)

print('{:02d}-{:02d}-{:4d}'.format(now.month,now.day,now.year))

def choice():
    print("请选择，左还是右")
    answer = input("输入 左 或者 右：")
    if answer == "左" or answer == "右":
        print("你选择左")
    elif answer == "右" or answer == "左":
        print("你选择右")
    else:
        print("你两个都没选")
        choice()