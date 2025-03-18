# 2025.03.18
# 파이썬 리스트 : 한개의 변수에 여러 값을 할당

colors = ['red', 'blue', 'black']
print(colors) # 전체 출력
print(colors[1]) # 두번째 출력
print(colors[-1]) # 마지막 출력
print(len(colors))

# 슬라이싱
cities = ['서울', '부산', '인천', '의정부', '대전', '강릉', '용산', '포항']
print(cities[0:8]) # cities[0:n] 0~n-1까지 출력
print(cities[:7])
print(cities[:-1])
print(cities[3:])
print(cities[:])
print(cities[-4:])
print(cities[:7:2])
print(cities[::3])
print(cities[::-1])
print(cities[4::-2])

# 리스트의 추가

colors.append('white')
print(colors[:])
colors.extend(['green', 'purple'])
colors.insert(1, 'orange')
print(colors)
colors.remove('purple')
print(colors)
colors[1] = 'sky'
print(colors)

# 패킹, 언패킹
c1, c2, c3,c4, c5, c6 = colors
print(c1,c2,c3)

# 퀴즈
first = ['egg','salad','bread','soup','canafe']
second = ['fish','lamb','pork','beef','chicken']
third = ['apple','banana','orange','grape','mango']
order = [first,second,third]
print(order)
john = [order[0][:-2], second[1::3], third[0]]
del john[2]
john.extend([order[2][0:1]])
print(john)