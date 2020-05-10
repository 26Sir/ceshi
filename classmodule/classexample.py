#!/usr/bin/python3
#conding=utf-8

class Person:
    total_person = 0

    def __init__(self, name, sex, province):
        #print("参数来了")
        self.name = name
        self.sex = sex
        self.province = province
        Person.total_person += 1

    def get_name(self):
        return self.name

if __name__=="__main__":
    person1 = Person("xiaosun","nan","shanxisheng ")
    print(person1.name,person1.sex,person1.province)

