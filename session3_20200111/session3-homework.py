#a = 'We are the champion'

#b = len(a.split())

#print(b)

#a = input()
#b = len(a.split())
#print(b)

# 로또 게임 만들기 1. 1부터 10까지 중복안되게 2. 10보다 큰 숫자는 안됌 3.문자도 안됌 4.

from random import randint

user_numbers = []
lucky_numbers =[]

print("1~10까지의 숫자를 입력하십시오.")
while 0<= len(user_numbers) < 5 :
    input_numbers = input("> ")

    try:
        a = int(input_numbers)
    except:
        print('무효한 값입니다. 다시 입력하세요.')
        continue
    if  0> a or a >10:
        print('1~10까지의 숫자를 입력해라.')
        continue
    elif a in user_numbers:
        print(user_numbers,"이외의 숫자를 입력하세요.")
        continue
    user_numbers.append(a)
print("당신이 고른 숫자는", user_numbers, '입니다.')