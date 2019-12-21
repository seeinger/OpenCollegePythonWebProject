# 리스트는 각각의 element의 의미를 부여하기 어렵다.

a = list()
a.append('010-1234-5678')
a.append('010-2343-1234')

fistValueinA = a[0] # 첫번쨰가 누구였지... 헷갈리게 됨

# 대안으로 나온 dictionary
b = {'김도한':['010-1234-1234','010-2323-1122'], '이용섭':'010-2342-2322'}

dohanValueinB = b['김도한']
print(type(dohanValueinB))

# key는 바꿀 수 없음

c = dict(김도한 = '복정', 이용섭 = '대전')
print(c)

# dict에 존재하지 않는 key를 검색할 경우
# d  = c['이근호'] -> 에러 발생
#print(d)

is_dohan_exist = "김도한" in c
print(is_dohan_exist)
is_heywon_exist = '조혜원' in c

if is_heywon_exist:
    print(c['조혜원'])
else:
    print('혜원님은 없습니다.')

c.pop('김도한') # 김도한 삭제
print(c)
c.clear()
print(c)

