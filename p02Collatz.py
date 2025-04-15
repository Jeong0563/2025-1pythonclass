#2025 04 01
#collatz 추측
#1부터 1000까지 숫자중, 가장 많은 단계를 거쳐서 1로 가는 수는 무엇인가, 가장 많은 단계는 몇단계인가
#n이 짝수 -> n/2
#n이 홀수 -> 3* n + 1
n = 1
ncopy = 0
count = 0
max_num = 0
max_num2 = 0
max_num3 = 0
ncount = 0
for n in range(1, 10):
    ncopy = n
    count = 0
    while n > 1:
        count+=1
        if n % 2 == 0:
            n = n / 2
        elif n % 2 != 0:
            n = 3 * n + 1
    print(count)
    if max_num < count:
        max_num2 = max_num
        max_num = count
        ncount2 = ncount
        ncount = ncopy
    elif max_num2 < count < max_num:
        max_num2 = count
print('숫자',ncount)
print('가장 높은 숫자', max_num)
print('두번째 숫자', ncount2)
print('두번째로 큰수', max_num2)