# 2-1
print(200, '+', 300, '+', 400, '=', 200 + 300 + 400)

#2-2
weight = 30
height = 60
print(weight)
print(height)

#2-5
side_length = int(input('정사각형의 밑변을 입력하시오: '))

area = side_length * side_length

print('정사각형의 면적:', area)

#2-6
print('1에서 10까지의 합:', 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10)

#2-10
celsius = int(input('섭씨온도를 입력하세요:'))
fahrenheit = (9 / 5) * celsius + 32
print("섭씨",celsius,'도는 화씨',fahrenheit,"도 입니다.")

#2-11
fahrenheit = int(input("화씨 온도를 입력하세요: "))
celsius = (fahrenheit - 32) * 5 / 9
print("화씨",fahrenheit,'도는 섭씨',celsius,"도 입니다.")
#2-12
radius = 11
PI = 3.141592

circumference = 2 * PI * radius
area = PI * radius ** 2

print("원의 반지름", '=', radius, "원의 둘레", '=', circumference, "원의 면적", '=', area)
