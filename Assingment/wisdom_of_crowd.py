import random
#import time
import matplotlib.pyplot as plt
from statistics import mean
from scipy import stats

#start = time.time()
e = []
elements = 75
while elements > len(e):
    r1 = random.randint(100, 2001)
    e.append(r1)

e.sort()
m = stats.trim_mean(e, 0.1)
print(m)
#tv = int(0.1 * len(e))
#e = e[tv:]
#e = e[:len(e) - tv]
#print(mean(e))
#end = time.time()
#print(float(end - start))

plt.plot(e)