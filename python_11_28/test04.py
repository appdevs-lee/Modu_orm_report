# 문자열 인덱싱
name = 'Guido van Rossum'
print(name[0])
print(name[1])
print(name[2])

# 문자열 슬라이싱
birth = "1994.08.13"
year = birth[:4]
month = birth[5:7]
day = birth[8:]
print("태어난 연도 : ", year)
print("태어난 월 : ", month)
print("태어난 일 : ", day)

explain = "위니브 월드 외각에 살고있는 생선가게 주인 캣(cat)"
print(explain[0:6]) # 슬라이싱을 쓸 때 내가 원하는 끝 인덱스 + 1로 적어줘야 한다. -> 매우 중요.
print(explain[2:6:2])
# 변수[시작 인덱스:끝 인덱스:증감폭]
# explain[0:6]은 explain[0:6:1]에서 :1이 생략되어 있는 것이다.

# 문자열 사칙연산
s = 'leehojun'

print(s+s)
print(s*3)
# s/s -> Error
# s//s -> Error
# s-s -> Error