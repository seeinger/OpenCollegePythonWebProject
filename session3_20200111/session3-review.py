# 더하기 2 3
# 5

def calc(type, a, b):
    if type == "더하기":
        return a + b
    elif type == '빼기':
        return a - b
    elif type == "곱하기":
        return a * b
    elif type == "나누기":
        return a / b

a = input()\
input_list = a.split()
type = input_list[0]
a = int(input_list[1])
b = int(input_list[2])
result = calc(type,a,b)
print(result)