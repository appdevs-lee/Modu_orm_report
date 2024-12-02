# FI = 3.14

# def f(r):
#     return FI * r * r

# print(f(3))

# def returnNumber(count):
#     if count > 100:
#         return
#     print(count)
#     return returnNumber(count + 1) #값을 1부터 반복횟수 까지의 값을 출력

# returnNumber(1)

# def factorial(n):
#     if n == 1:
#         return 1
#     return factorial(n-1) * n

# print(factorial(5))

"""
I
love
python

"""
# def plus(num1, num2):
# 	#이곳을 채워주세요
#     return num1 + num2

# def minus(num1, num2):
# 	#이곳을 채워주세요
#     return num1 - num2

# def multiply(num1, num2):
# 	#이곳을 채워주세요
#     return num1 * num2

# def divide(num1, num2):
# 	#이곳을 채워주세요
#     return num1 / num2

# print(f'plus : {plus(10, 5)}')
# print(f'minus : {minus(10, 5)}')
# print(f'multiply : {multiply(10, 5)}')
# print(f'divide : {divide(10, 5)}')

def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n-1)

print(power(4, 5))