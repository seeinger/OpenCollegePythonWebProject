# in 뒤에는 무조건 iterable 이 와야 한다.

friends = ['미아','이유','은지','메롱','짱구']
for friend in friends:
    print('친구' + friend)


# for 임시상자 in iterable type :
    #print(임시상자)

number = list(range(1,10))
print(number)

for i in number :
    print(i * "*")

a = {'김도한':'010-2222-2222', '신봉건':'010-2222-3333'}

for name in a.keys():
    print(name)

for phone_number in a.values():
    print(phone_number)

