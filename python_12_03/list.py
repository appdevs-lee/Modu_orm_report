# #1차원 리스트
# a = [100000, 2, 1, 3]
# print(type(a))

# a = list()
# print(type(a))

# a = list('leehojun') #형변환
# print(type(a))

# print(a)
# print(a[0])

#2차원
# a = [[1, 2, 3],
#      [11, 22, 33],
#      [10, 2000, 30]]
# max(a)
# min(a)
# # sum(a)
# print(max(a, key=lambda x:x[1])) 
# print(min(a, key=lambda x:x[1]))
# print((lambda x:x[1])(a))
# sum(a) error
# sum(a, [])

#2차원
# a = [[1, 2, 3],
#      [11, 22, 33],
#      [13, 20000, 300000]]

# for i in a:
#     print(i)

# #요소별로 순회하기
# for i in a:
#     print(i)
#     for j in i:
#         print(j)

# print(list(range(100)))
# print(list(range(5, 10)))

# #print(list(range(start, stop, step)))
# print(list(range(0, 101, 2))) #짝수
# print(list(range(1, 101, 2))) #홀수

# print(list(range(5,101,5)))
# print(list(range(10,101,10)))

# print(list(range(100, 1, -2)))

# print(list(range(-1, -101, -1)))

# l = []
# for i in range(10):
#     l.append(i)

# ll = [i for i in range(10)]

# a = [i for i in range(1, 100) if i %3 == 0 or i %5 == 0]
# print(a)

# -1 ~ -100 
# a = [i for i in range(-1, -101, -1)]
# b = [i for i in range(1, 101) if i % 2 == 0 or i % 8 == 0]
# print(a)
# print(b)

# a = [f'{i} X {j} = {i*j}' for i in range(2, 10) for j in range(1, 10)]
