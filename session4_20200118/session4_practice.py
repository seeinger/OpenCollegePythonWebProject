class Car:
    def __init__(self,manufactor,model,color):
        self.manufactor = manufactor
        self.model = model
        self.color = color
        self.left_oil = 1000

    def advance(self):
        self.left_oil -= 50
        print(self.manufactor,self.model,self.color,'차량 전진중입니다! 현재 기름양 : ', self.left_oil)

    def backward(self):
        self.left_oil = self.left_oil - 30
        print(self.manufactor,self.model,self.color,'차량 후진중입니다! 현재 기름양 : ', self.left_oil)

class ElectricCar(Car):
    def __init__(self, manufactor, model, color,battery = 100):
        super().__init__( manufactor, model, color)
        self.battery = battery
    def advance(self):
        self.battery -= 10
        print(self.manufactor,self.model,self.color,'차량 전진중입니다! 현재 충전량:', self.battery,'입니다.')

    def backward(self):
        self.battery -= 5
        print(self.manufactor,self.model,self.color,'차량 후진중입니다! 현재 충전량 : ', self.battery,'입니다')

tesla = ElectricCar('현대','제네시스','블랙')
tesla.advance()
tesla.backward()
#hyundai = Car('현대','k5','블랙')
#bmw = Car("bmw",'530d','화이트')
#hyundai.advance()
#hyundai.backward()
#bmw.advance()
#bmw.backward()