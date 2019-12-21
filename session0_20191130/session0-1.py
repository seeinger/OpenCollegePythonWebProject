# a라는 박스에 2를 넣는다/
# = 은 같다라는 뜻이 아니다. 저장한다는 뜻이다!!
from typing import Type

a = 2
b = 3.14
c = "안녕하세요"
print(a)
print(b)
print(c)

type_a = type(a)
type_b = type(b)
type_c = type(c)

print(type_a)
print(type_b)
print(type_c)
