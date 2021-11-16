# class1.py

class Person:
    # 생성자
    def __init__(self):
        self.name = "default name"
    def print(self):
        print("My name is {0}".format(self.name))

p1 = Person()
p1.name = "전우치"        
p2 = Person()
p1.print()
p2.print()