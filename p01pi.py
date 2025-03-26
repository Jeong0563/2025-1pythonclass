# 오일러 공식을 이용한 파이구하기

n_terms = 100
pi_approx = 1
for i in range(1,n_terms):
    pi_approx *= ((2*i+1)**2-1) / ((2* i + 1) **2)
print(pi_approx * 4)

n = 1
p=1
p *= ((2*n+1)**2-1) / ((2*n +1)**2)
print(p * 4)
n = 2
p *= ((2*n+1)**2-1) / ((2*n +1)**2)
print(p * 4)

import matplotlib.pyplot as plt
plt.plot([1,2,3])
plt.show()