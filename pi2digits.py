import numpy as np
import re

freq = [0]*10
file = open("pi-billion.txt", "r")
pi = file.read()
#del pi[1]
#del pi[-1]

nums = ["{0:02}".format(i) for i in range(10)]
for i in nums:
    pattern = str(i)
    freq[int(i)] = len(re.findall(pattern, pi))

print(freq)
#print(min(freq))
#print(freq.index(min(freq)))
#print(max(freq))
#print(freq.index(max(freq)))
#sum = 0
#for i in freq:
#    sum += i
#print(sum)
#print(len(pi))
