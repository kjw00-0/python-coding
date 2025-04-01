#4.1
for i in range(9):
    print('2*', i+1, '=', 2*(i+1))

#4.1
i=0
while i<9:
    print('2*', i+1, '=', 2*(i+1))
    i+=1
    

#4.3

for i in range(3):
    print('phyton')
    print('is')
    print('Fun!')



for i in range(3):
    print('phyton')
    print('is')
print('Fun!')


for i in range(3):
    print('phyton')
print('is')
print('Fun!')

#4.5
print('맛나 식당에 오신 것을 환영합니다. 메뉴는 다음과 같습니다.')
print('-햄버거(입력b)')
print('-치킨(입력c)')
print('-피자(입력p)')
selected = input('메뉴를 선택하세요:')
while selected not in ['b', 'c', 'p']:
    selected = input('메뉴를 다시 입력하세요:')
    break
print(selected, '을(를) 선택하였습니다')

#4.7

#4.9
n=int(input('숫자를 입력하세요:'))
a=0
for i in range(1,n+1):
    a+=i**2
print('결과는 ', a, '입니다.')

#4.11

#4.13
n=[]
for num in range(100, 1000):
    hun=num//100
    tens=(num//10)%10
    ones=num%10

    if (hun**3+tens**3+ones**3)==num:
        n.append(num)
print('세 자리 암스트롱 수: ', n)

