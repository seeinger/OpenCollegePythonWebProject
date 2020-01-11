# parameter의 디폴트는 중간부터 적용 못함/ 오른쪽 끝부터 적용

def add(a, b = 2):
    return a+ b

print(add(1,2))
print(add(1))

# local 변수 global 변수

a = 2
def changeA():
    global a
    a = 3
    print(a)

number_list = [1,2,3,4]
sum = 0
for a in number_list:
    sum = sum + a
    print(sum)