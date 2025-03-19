#2-13
PI = 3.141592

radius = int(input("원의 반지름을 입력하세요: "))


circumference = 2 * PI * radius
area = PI * radius ** 2

print('원의 둘레','=', circumference,'원의 면적','=',area)

#2-15
width = int(input("밑변을 입력하세요 : "))
height = int(input("높이를 입력하세요 : "))

hypotenuse = (width**2 + height**2) ** 0.5

print("빗변 :", hypotenuse)

#2-18
n = int(input("정수를 입력하세요 : "))

if n % 2 == 0:
    print('이 수가 짝수인가요?',True)
else:
    print("이 수가 짝수인가요?",False)

#2-19
n = int(input("정수를 입력하세요: "))

if 0 <= n <= 100 and n % 2 == 0:
    print("입력된 정수는 0에서 100의 범위 안에 있는 짝수인가요?", True)
else:
    print("입력된 정수는 0에서 100의 범위 안에 있는 짝수인가요?", False)
#2-22
a = int(input("정수 a를 입력하세요: "))
b = int(input("정수 b를 입력하세요: "))

Q = a // b
R = a % b

print("a / b의 몫 :", Q)
print("a / b의 나머지 :", R)

#2-23
n = int(input("세 자리 정수를 입력하세요: "))

H = n // 100
T = (n // 10) % 10
O = n % 10

print("백의 자리:", H)
print("십의 자리:", T)
print("일의 자리:", O)

#2-24
n = int(input("세 자리 정수를 입력하세요: "))

H = n // 100
T = (n // 10) % 10
O = n % 10

print(O)
print(T)
print(H)

