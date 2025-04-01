# 오일러 공식을 이용한 파이구하기

# n = 1
# p=1
# p *= ((2*n+1)**2-1) / ((2*n +1)**2)
# print(p * 4)
# n = 2
# p *= ((2*n+1)**2-1) / ((2*n +1)**2)
# print(p * 4)

pilist = []

p = 1
for i in range(1,200):
    p *= ((2*i+1)**2-1) / ((2* i + 1) **2)
    pilist.append(p*4)
    print(p * 4, ',')

import matplotlib.pyplot as plt
plt.plot(pilist)
plt.show()
