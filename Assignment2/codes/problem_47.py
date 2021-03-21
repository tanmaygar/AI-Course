import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from scipy.stats import norm
from scipy.stats import binom

k = 100000

data_bern = bernoulli.rvs(size=k,p=0.2)
print(data_bern)
theta = 0.1
count = 0
for i in data_bern:
  choose_N = np.random.uniform(-2, 2, None)
  if i == 0:
    Y = 1 + choose_N
    if Y <= -1:
      count = count + 1
  if i == 1:
    Y = -1 + choose_N
    if Y >= -1:
      count = count + 1

    
print("The minimum probability is: " , count/k)
