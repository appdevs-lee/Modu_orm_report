# b = [1,2,3,4]

# b.extend([5,6,7])

# print(b)

# a = [10, 1, 1, 11, 2, 23, 12]
# print(a.pop()) # O(1)
# print(a.pop(2)) # O(N)

# a.reverse() # a[-1::-1]
# b = list(reversed(a))

# print(a)
# print(b)

# # a.sort()
# print(a)
# c = list(sorted(a, reverse=True))
# print(c)

l = [[1, 10, 'leehojun'], 
     [20, 30, 'hojun'], 
     [10, 20, 'weniv!'], 
     [1, 2, 'hello world'], 
     [55, 11, 'sun']]

# 1. 글자 수 대로 정렬해주세요.
def textCount(list):
    return list[2].count

print(sorted(l, key=textCount(l), reverse=True))
# 2. 맨 앞에 위치한 숫자대로 정렬해주세요.

# 3. 중앙에 위치한 값대로 정렬해주세요.