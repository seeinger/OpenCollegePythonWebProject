menu = {'라면': 4000, '만두': 3500, '보쌈':28000}

a = input('메뉴를 입력하세요 : ')

if a in menu:
    cost = menu[a]
    print(a + '의 가격은' +str(cost) + '원 입니다.')
else :
    print(a + '란 메뉴는 없습니다.')

