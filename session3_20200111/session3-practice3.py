def calcMax(number_list):
    max = number_list[0]
    for number in number_list:
        if number > max:
            max = number
    return max

def calcMin(number_list):
    min = number_list[0]
    for number in number_list:
        if number < min:
            min = number
    return min

def calcAvg(number_list):
    sum = 0
    for number in number_list:
        sum = sum + int(number)
    return sum / len(number_list)



numbers = input("숫자를 입력하세요")
min_result = calcMin(numbers.split())
max_result = calcMax(numbers.split())
avg_result = calcAvg(numbers.split())

print("최솟값" + str(min_result))
print("최댓값" + str(max_result))
print("평균" + str(avg_result))

a = input("test : ")
print(type(a))