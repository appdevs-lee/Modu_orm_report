# print(type(int(3.5)))
# print(int(3.5))
# print(type(float(3)))
# print(float(3))
# print(type(str(3)))
# print(str(3))

# x = input('Insert the number.')
# y = input('Insert the number.')
# print(x + y)
# print(type(x))
# print(type(y))

# num = '123'
# print(type(num))
# print(type(int(num)))
      
# string = 123
# print(type(string))
# print(type(str(string)))

# print("bool('test') : ", bool('test'))
# print("bool(1) : ", bool(1))
# print("bool(0) : ", bool(0))
# print("bool(-1) : ", bool(-1))
# print("bool(' ') : ", bool(' '))
# print("bool('') : ", bool(''))
# print("bool(None) : ", bool(None))

s='10'
print(float(s))

s='10000'
print(float(s))

s='10'
l=list(s)
print(l)

name='LeeHoJun'
print(list(name))

name='LeeHoJun'
print(tuple(name))

# name='LeeHoJun'
# print(dict(name))

s=[('name','LeeHoJun'),('age',10)]
d=dict(s) # {'name': 'LeeHoJun', 'age': 10}
print(d)

name='LeeHoJun'
print(set(name)) #중복을 허락하지 않고 순서가 없습니다.
print(len(set(name))) #중복을 제거한 상태로의 길이를 알려줍니다.
print(len(name))

a = input("문자를 입력해주세요.") * 2
print(a)