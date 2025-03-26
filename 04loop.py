# 0326 2학년 1학기 파이썬 수업
# 반복문

for i in range(10):
    print(f'{i=}')

for j in range(1, 10, 2):
    print(f'{j=}')

for looper in [1, 2, 3, 4, 5, 'end']:
    print(f'{looper=}')

cities = ['서울', '부산', '인천', '의정부', '대전', '강릉', '용산', '포항']
for city in cities:
    print(f'{city=}')

string = "python"
for c in string:
    print(f'{c=}')

i = 1
while i < 10:
    print(f'{i=}')
    i += 2

#1부터 100까지 홀수의 합
h = 0
for i in range(1, 101, 2):
    print(i)
    h += i

print(h)

h = 0
for i in range(0, 101, 2):
    print(i)
    h += i

print(h)
h = 0
i = 0
while i < 101:
    if i % 2 == 0:
        h += i
    i += 1
print(h)
