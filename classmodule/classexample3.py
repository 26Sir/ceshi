#!/usr/bin/python3
#conding=utf-8

from selenium import webdriver


from classmodule.classexample2 import Student
from classmodule.classexample1 import Person

class SeniorStudent(Student):
    def __init__(self,name,sex,province,grade):
        #super(SeniorStudent,self).__init__(name,sex,province,grade)
        Student.__init__(self,name,sex,province,grade)
        self.grade = grade
    def get_grade(self):
        return self.grade
    def get_name(self):
        return "名字不可说"

    def overtime_study(self):
        if self.grade == 3:
            return "补课"
        else:
            return "不补课"

    def new_sex(self):
        sex = Person.get_sex()

if __name__ == "__main__":
    aa = SeniorStudent("husan","nan","shanxi",3)
    print(aa.overtime_study(),aa.get_name())