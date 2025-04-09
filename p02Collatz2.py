import numpy as np
import statistics
import time
from p02Collatzfunc import collatz
#2025 04 09 2번째  기본 통계량 구하기
# 평균, 중앙값, 표준편차, 최빈값
max_num = 100

#리스트

start = time.time()
ncountl =[]
for n in range(1, max_num):
    ncount = collatz(n)
    ncountl.append(ncount)


# print(sum(ncountl)/ len(ncountl))
print(f'최대값은 = {max(ncountl)}')
print(f'중앙값은 = {statistics.median(ncountl)}')
print(f'표준편차는 = {statistics.stdev(ncountl): .3f}')
print(f'평균은 = {statistics.mean(ncountl): .3f}')

end = time.time()

print(f'{end - start: .5f}초')

# 넘파이
start1 = time.time()
ncounta = np.zeros(max_num-1)

for n in range(1, max_num):
    ncount = collatz(n)
    ncounta[n-1] = ncount


print(f'중앙값은 = {np.median(ncounta)}')
print(f'표준편차는 = {np.std(ncounta): .3f}')
print(f'최대값은 = {np.max(ncounta)}')
print(f'평균은 = {np.mean(ncounta): .5f}')

end1 = time.time()
print(f'{end1 - start1: .5f}초')