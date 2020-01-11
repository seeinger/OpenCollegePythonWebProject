def calculator(calcType, a, b) :
    if calcType == "add":
        return a + b
    elif calcType == "sub":
        return a - b
    elif calcType == "mul":
        return a * b
    elif calcType == "div":
        return a / b
    else:
        return "올바른 계산 타입이 아닙니다."

# parameter(재료,인자,매개변수) 가 없는 함수
def sayGoodbye():
    return "Good bye"
try:
    result1 = calculator("add", 2, 3)
    result2 = calculator("sub", 2, 3)
    result3 = calculator("mul", 2, 3)
    result4 = calculator("div", 2, 3)
    result5 = calculator("div", 2, 0)
    print(result1,result2,result3,result4,result5)
except:
    print("error 발생했습니다.")

print(sayGoodbye())

def printGoodbye():
    print(sayGoodbye())
printGoodbye()