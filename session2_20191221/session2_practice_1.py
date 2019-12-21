numbers = [1,100,-1,30,5,99,45,30,-2,-10]

# 최댓값과 최솟값을 1이라 가정하자
max = numbers[0]
min = numbers[0]

for i in numbers:
    if i > max:
        max = i
    if i< min:
        min = i

print('최댓값은' + str(max) + '입니다.')
print('최솟값은' + str(min) + '입니다.')


