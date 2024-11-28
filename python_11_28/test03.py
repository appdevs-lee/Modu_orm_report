# 자료형 검증
# A = 486
# B = 0b100
# C = 0o56
# D = 0xAC
# E = 3.14
# F = 4-4j

# print(type(A))
# print(type(B))
# print(type(C))
# print(type(D))
# print(type(E))
# print(type(F))

# 문자 자료형
# a = 'DEV LeeJuSung'
# b = 'DEV LeeJuSung'
# c = "DEV \\'LeeJuSung'"
# d = 'DEV \'LeeJuSung\'' 
#같은 종류의 따옴표를 사용하고 싶으면 이스케이프 문자를 사용해야 합니다. 
# print(a, b, c, d)

# valString = 'abc'
# valList = [1, 2, 3]
# valTuple = (1, 2, 3)
# print(valString[0])
# print(valString[1])
# print(valString[2])
# print(valList[0])
# print(valList[1])
# print(valList[2])
# print(valTuple[0])
# print(valTuple[1])
# print(valTuple[2])

# s = 'paullab CEO leehojun'
# print(s.lower()) #전체를 소문자로 바꿔주는 method
# print(s.upper()) #전체를 대문자로 바꿔주는 method

# s = 'paullab CEO leehojun'
# # 문자열을 찾아서 index를 반환해주는 method 
# print(s.find('CEO')) # 없을 경우 : -1(해당 부분이 error를 발생시키지 않기 때문에 선생님은 더 선호함.)
# print(s.index('CEO')) # 없을 경우 : ERROR

# s = 'paullab CEO leehojun'
# print(s.count('')) #문자열이나 숫자를 셀 때 사용
"""
str.count의 정의(python 공식 문서 참조)
[ start , end ] 범위 내에서 substring sub 의 겹치지 않는 발생 횟수를 반환합니다 . 선택적 인수 start 및 end는 슬라이스 표기법으로 해석됩니다.
sub가 비어 있으면 , 문자열의 길이에 1을 더한 값인 문자 사이의 빈 문자열의 개수를 반환합니다.
"""
"""
강사님 답변
예를 들어 'abc'라는 문자열이 있다고 해볼까요?

빈 문자열은 이렇게 들어갈 수 있어요.

⭐a⭐b⭐c⭐

⭐로 표시한 부분이 빈 문자열이 들어갈 수 있는 자리예요!

문자열 시작 전(1개), 각 문자 사이(2개), 문자열 끝(1개) = 총 4개인거죠 ㅎㅎ

즉 아무 문자열이나 길이가 n이면, 빈 문자열은 항상 n+1개가 나오는 거죠  🙂
"""
# print(len(s))
"""
len의 정의(python 공식 문서 참조)
Return the length (the number of items) of an object. The argument may be a sequence (such as a string, bytes, tuple, list, or range) or a collection (such as a dictionary, set, or frozen set).
CPython implementation detail: len raises OverflowError on lengths larger than sys.maxsize, such as range(2 ** 100).
"""

# print('    ,!!  hello world   '.strip(' ,!'))
#양쪽의 공백과 ',!'을 제거해주는 method

# print('   ,!!  hello world   '.replace(' ', ''))
#다른 문자로 교체해주는 method

#메서드 체이닝 : 연속해서 다른 method들을 실행합니다.
# print('   ,!!  hello world   '.replace(' ', '').replace(',', '').replace('!', ''))

# split 메서드
#문자열을 쪼개어 줍니다.
# print('paullab CEO leehojun'.split(' '))
# print('paullab!CEO!leehojun'.split('!'))
# print('paullab,CEO,leehojun'.split(','))

# join 메서드
#쪼개어진 문자열을 합쳐줍니다.
# print('~'.join(['paullab','CEO','leehojun']))
# print('!'.join(['paullab','CEO','leehojun']))

# isdigit() / isalnum( ) / isdigit() / isalpha( ) / isascii( )
# 숫자인지 아닌지 판단해줍니다.
# print('paullab CEO leehojun'.isdigit())
# print('123'.isdigit())

# 알파벳인지 아닌지 판단해줍니다.
# print('paullab CEO leehojun'.isalpha())
# print('123'.isalpha())

# 알파벳이거나 숫자인지 아닌지 판단해줍니다.
# 권장하지는 않음.
# print('paullab CEO leehojun'.isalnum())
# print('123'.isalnum())

# 아스키코드인지 아닌지 판단해줍니다.
# print('paullab CEO leehojun'.isascii())
# print('123'.isascii())

# rjust() / ljust() / center()
# print('paullab CEO leehojun'.rjust(30)) #오른쪽 정렬
# print('paullab CEO leehojun'.ljust(30)) #왼쪽 정렬
# print('paullab CEO leehojun'.center(30))#가운데 정렬

# zfill()
# print('paullab CEO leehojun'.zfill(30)) #빈 공간을 채워줍니다.
# print('paullab CEO leehojun'.zfill(30).replace('0','!'))

# bin(30)[2:]
# bin(30)[2:].zfill(8)