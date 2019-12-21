numbers = [1,2,3,4]
numbers_double = []

for a in numbers:
    numbers_double.append(a * 2)

for a in numbers_double:
    print(a, end="")

# for문 한 줄에 쓰기 (list comprehension)

numbers_double2 = [number * 2 for number in numbers]
