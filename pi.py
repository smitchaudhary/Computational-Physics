import numpy as np
import matplotlib.pyplot as plt

def normalized(freq, n):
    freq1 = [0]*10
    for i in range(10):
        freq1[i] = freq[i]/n
    return freq1

file = open("pi1000000.txt", "r")
pi = file.read()

freq = [0]*10
pi = list(pi)
del pi[1]
del pi[-1]
pi = list(map(int, pi))

count = 0

for i in pi:
    freq[i] += 1
    count += 1
    if count%100000 == 0:
        freq1 = normalized(freq,count)
        plt.plot(freq1)
        plt.show()
