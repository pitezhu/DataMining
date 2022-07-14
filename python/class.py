class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.other = 0

    def sit(self):
        print(self.name+' is sit')

    def roll(self):
        print(self.name+' is roll')

    def info(self):
        print(self.name+' is '+self.age)


mydog = Dog('pisa', 4)
mydog.sit()
print(mydog.name)  # 用句点访问属性和方法
mydog.name = 'sa'
mydog.sit()


class SmallDog(Dog):
    def __init__(self, name, age, big):
        super().__init__(name, age)
        self.size = 12
        self.big = big

    def samll(self):
        print(self.size)
        print(self.big)


mysamlldog = SmallDog('ds', 20, 11)
mysamlldog.samll()
