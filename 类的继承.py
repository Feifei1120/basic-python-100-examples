class Audi(Car):  #这里的Car就是父类，这里没把Car的类给写出来666666666666666
    def __init__(self,type):
        self.brand = 'Audi'
        print(self.type)
        
CarA = Car("BMW")
CarA.car_brand()
CarB = Audi("A4") #初始化一个对象
CarB.car_brand()  #调用了一个方法