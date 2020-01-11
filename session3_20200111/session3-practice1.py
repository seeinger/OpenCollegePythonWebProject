# 코딩해보기

def calc(type, a, b):
    if type == '더하기':
        return a+b
    elif type == '빼기':
        return a-b
    elif type == '나누기':
        return a/b
    elif type == '곱하기':
        return a*b

a = input('계산정보를 입력하세요: ')
input_list = a.split()
type = input_list[0]
a = int(input_list[1])
b = int(input_list[2])
result = calc(type, a, b)
print("계산결과:" + str(result))
