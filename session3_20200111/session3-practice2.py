def calcMax(number_list):
    return max(number_list)

def calcMin(number_list):
    return min(number_list)

def calcAvg(number_list):
    sum = 0
    for a in numbers:
        sum = sum + a
    return sum / len(numbers)

numbers = input("숫자들을 입력하세요: ")
max_result = calcMax(numbers.split())
min_result = calcMin(numbers.split())
avg_result = calcAvg(numbers.split())

print("최댓값 : " + str(max_result))
print("최솟값 : " + str(min_result))
print("평균값 : " + str(avg_result))