# if문
a = 2
b = 3

if a == b :
    print("a와 b는 같다")
else:
    print('a와 b는 다르다')

# if 두에는 bollean 타입이다.
if True:
    print('항상 참이야')

result = input('시험 점수를 입력하세요.')

if int(result) >=  90:
    print('축하합니다. A등급입니다.')
elif int(result) >= 80:
    print('축하합니다! B등급입니다.')
else:
    print('불합격입니다.')

