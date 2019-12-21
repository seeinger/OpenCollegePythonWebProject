# input의 결과는 무조건 string

a = input()
b = a.split()
result = int(b[0]) + int(b[1])
print(result)

numbers = input()
result = int(numbers.split())
if result[0] > result[1]:
    print('>')
elif result[0] < result[1]:
    print('<')
else:
    print('==')