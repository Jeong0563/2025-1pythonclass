#2025 04 01
#collatz 추측
#1부터 1000까지 숫자중, 가장 많은 단계를 거쳐서 1로 가는 수는 무엇인가, 가장 많은 단계는 몇단계인가
#n이 짝수 -> n/2
#n이 홀수 -> 3* n + 1
n = 1
n1 = 0
j = 0
num = 0
num1 = 0
for n in range(1, 10):
    n += 1
    n1 = n
    j = 0
    print(n)
    while n > 1:
        j+=1
        if n % 2 == 0:
            n = n / 2
            print('짝수', 'n / 2 = ',n)
        elif n % 2 != 0:
            n = 3 * n + 1
            print('홀수', '3*n+1 = ', n)
        if num < j:
            num = 0
            num += j
            num1 = n1

        print('반복횟수', j)
print('높은 숫자',num1)
print('가장 높은 숫자', num)