# list 조작

openCollegeSatPython = list()
openCollegeSatPython.append('은지님')
openCollegeSatPython.append('혜원님')
openCollegeSatPython.append('근호님')
openCollegeSatPython.append('선혜님')
openCollegeSatPython.append('용섭님')
openCollegeSatPython.append('하경님')

print(openCollegeSatPython)

openCollegeSatPython.remove('선혜님')
print(openCollegeSatPython)

# sort() 메소드
a = [-1,2,100,0,4]
a.sort()
print(a)
a.sort(reverse=True)
print(a)
b = [1,2,100,-100,-200]
c = sorted(b, reverse=True)
print(b)
print(c)

# tuple는 꽁꽁얼린 list / 변경 불가능한 list
a = ('은지','용섭','하경','근호','혜원')
print(a)
