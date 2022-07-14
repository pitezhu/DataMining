class Car():
    def __init__(self,name,color):
        self.name=name
        self.color=color

    def Info(self):
        print("Audo is my Car,color is red!")
#继承
class ELECar(Car):
    def __init__(self,name,color):
        super().__init__(name,color)

mycar=ELECar('Audo','red')
mycar.Info()
print(mycar.name)