# return value가 여러개인 함수

def multiplyAndDiv(a,b):
    return a * b , a / b

def calc(a,b):
    return a+b, a-b, a*b, a/b
print(type(multiplyAndDiv(1,2)))

result = calc(2,3)
print(result)

multiplyResult , divideResult = multiplyAndDiv(2,3)
print(multiplyResult)
print(divideResult)

