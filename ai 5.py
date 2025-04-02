#6-1
list_ex = [10, 20, 30, 40, 50, 60, 70]
high = 5
low = 3

list_ex[low]
40
list_ex[low + 2]
60
list_ex[high - low]
30
list_ex[low - high]
60
list_ex[-1]
70
list_ex[-low]
50
list_ex[2 * 3]
70
list_ex[2] * 3
90
list_ex[5 % 4]
20
len(list_ex)
7

#6-3
list1 = [3, 5, 7]
list2 = [2, 3, 4, 5, 6]

for num1 in list1:
    for num2 in list2:
        result = num1 * num2
        print(num1, '*', num2, '=', result)
        
#6-5
list1 = ['I like', 'I love']
list2 = ['pancakes.', 'kiwi juice', 'espresso.']

for a1 in list1:
    for a2 in list2:
        print(a1, a2)

#6-7
n_list = [10, 20, 30, 40, 50, 60]

total = 0

for num in n_list:
    total += num

print('합:', total)

#6-9
n_list = [10, 20, 30, 40, 50, 60]

max_v = n_list[0]

for num in n_list:
    if num > max_v:
        max_v = num

print('리스트 원소들:', n_list)
print('리스트 원소들 중 최대값:', max_v)

#6-11
n_list = []
for i in range(5):
    num = int(input('숫자를 입력하세요:'))
    n_list.append(num)


total = sum(n_list)  
average = total / len(n_list) 
max_v = max(n_list)
min_v = min(n_list)


print('입력된 값들:', n_list)
print('합:', total)
print('평균:', average)
print('최댓값:', max_v)
print('최솟값:', min_v)

#6-13

#6-15
greet = 'Have a beautiful day.'
result = greet[0:4] 
print(result)
result = greet[7:17]
print(result)
result = greet[17:21]
print(result)

#6-17-1
animals = ['dog', 'cat', 'tiger', 'lion']
print(animals)

#6-17-2
animals = ['dog', 'cat', 'tiger', 'lion']
animals.append(animals.pop(0))
print(animals)

#6-17-3
animals = ['dog', 'cat', 'tiger', 'lion']

#6-19


for animal in animals:
    print('I love ' + animal)

#6-19
s_list = ['abc', 'bcd', 'abc', 'abba', 'cddc', 'opq', 'opq']

new_s_list = [] 

for i in s_list:
    if i not in new_s_list:
        new_s_list.append(i)

print('s_list =', s_list)
print('new_s_list =', new_s_list)
