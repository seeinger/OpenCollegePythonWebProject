class Human:
    # constructor (생성자) 실제 object를 만드는 함수
    def __init__(self,gender,name,age,blood,):
        self.name = name
        self.gender = gender
        self.age = age
        self.blood = blood

    def ageDouble(self):
        self.age = self.age*2

    def introself(self):
        print("제이름은", self.name, '입니다. 나이는', self.age, '이고',self.blood,'형 입니다.')
hakyung = Human("female", '김하경', 19, 'B')
hakyung.introself()
hakyung.ageDouble()
hakyung.introself()

youngsub = Human('male','이용섭',20,"o")
youngsub.introself()
