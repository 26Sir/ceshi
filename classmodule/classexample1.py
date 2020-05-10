#!/usr/bin/python3
#conding=utf-8

class Person:
    def get_name(self):
        return self.name

    def set_name(self,name,sex):
        self.name= name
        self.sex = sex
    def get_sex(self):
        return self.sex

if __name__=="__main__":
    person1 = Person()
    person1.set_name("zhangsan","nv")
    print(person1.get_name())
    print(person1.get_sex())