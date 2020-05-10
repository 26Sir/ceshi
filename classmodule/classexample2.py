#!/usr/bin/python3
#conding=utf-8
from classmodule.classexample import Person
class Student(Person):
    def __init__(self,name,sex,province,grade):
        #连带父类一起初始化
        super(Student,self).__init__(name,sex,province)
        #只初始化父类
        #Person.__init__(name,)
        self.grade = grade
    def get_grade(self):
        return self.grade
    #多态，对父类中的方法进行重写,实现不同的业务逻辑
    def get_name(self):
        name1 = str(Person.get_name(self))
        if name1.startswith("zhang"):
            return "你是"+name1
        else:
            return name1

        # return "名字不可说"
    #派生，子类中实现新的方法
    def get_nick_name(self):
        #name = Person.get_name(self)
        name = str(Person.get_name(self))
        if name.startswith("xiao"):
            return "small"+name
        else:
            return name
if __name__=="__main__":
    ss = Student("zhangpeng","nan","shanxisheng",4)
    print(ss.get_name())
    # print(ss.get_grade())
    # print(ss.get_nick_name())