#!/usr/bin/python3
#conding=utf-8

class Person:
    total_person = 0
    def __init__(self,name,grade,provice):
        print("逼逼赖赖")
        self.name = name
        self.grade = grade
        self.provice = provice
        Person.total_person += 1

    def get_name(self):
        return self.name

    def set_name(self,name,sex):
        self.name= name
        self.sex = sex
    def get_sex(self):
        return self.sex

    @staticmethod
    #静态方法，可以被类或类的实例对象调用
    def set_new_name(new_name):
        return "new name is " +new_name

    @classmethod
    #类方法，可以被类或类的实例对象调用
    def set_new_provice(cls,new_provice):
        return "The new provice " + new_provice

    @property
    def new_grade(self):
        return self._new_grade
    @new_grade.setter
    def new_grade(self,value):
        self._new_grade = value




if __name__=="__main__":

    # print(Person.set_new_provice("ss"))

    # print(Person.set_new_name("six")

    per1 = Person("hhkk","2","sixss")
    per1.new_grade = "sssdsdadaddw"
    print(per1.new_grade)
    print(per1.get_name())
    print(per1.set_new_name("sool"))

    # person1 = Person()
    # person1.set_name("zhangsan","nv")
    # print(person1.get_name())
    # print(person1.get_sex())