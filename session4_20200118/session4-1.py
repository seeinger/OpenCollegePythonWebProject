class movie:
    def __init__(self,title,actor,director,genre):
        self.title = title
        self.actor = actor
        self.director = director
        self.genre = genre

    def book(self):
        print(self.title, "예약되었습니다.")
        print('장르는',self.genre,'입니다.')

class Actionmovie(movie):
    def __init__(self,title,actor,director,genre,nation):
        super().__init__(title,actor,director,genre) # super class의 constructor 중복으로 안 쓰고 상속받기
        self.nation = nation
    def book(self): # override 기능 (super에 있는 book기능은 없어진다.)
        #print('액션영화',self.title,'예약되었습니다.')
        #print('국가는',self.nation,'입니다.')
        super().book() # super 함수 살리면서 추가하는 방법
        print(self.title,'은 액션영화 입니다.')
malepicent = movie("malepicent",'angelina','hakyung','fantasy')
malepicent.book()

born = Actionmovie('born ultimatum','mat','dohan','action','america')
born.book()

