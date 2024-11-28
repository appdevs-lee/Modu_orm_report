# a = input("숫자를 입력하세요: ")
# 입력한 숫자는 문자열로 저장된다.

# print(a)

age = input('age를 입력하세요:')
lastname = input('lastname을 입력하세요:')
firstname = input('firstname을 입력하세요:')
print('당신의 이름은 ', lastname + firstname, '입니다.')
print('당신의 나이는 ', age, '입니다.')

name = lastname + firstname
print('1. 제 이름은 ', name, '입니다. 제 나이는 ', age, '입니다')
print(f'2. 제 이름은 {name}입니다. 제 나이는 {age}입니다.')
print('3. 제 이름은 {}입니다. 제 나이는 {}입니다.'.format(name, age))
print('4. 제 이름은 %s입니다. 제 나이는 %d입니다.'%(name, age))

"""
2번 같은 경우에 python 3.6 버전 이상에서 지원한다.
`f-string`이라고 불린다.
python 3.6버전 이전에는 .format을 많이 사용했었다.
최근에는 2번이 제일 많이 사용되고, 4번은 잘 사용하지 않는다.
"""