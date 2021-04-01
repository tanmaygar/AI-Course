import math

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from scipy.stats import norm
from scipy.stats import binom
from scipy.stats import poisson

#number of test cases
k = 100000
count = 0
data_first30 = poisson.rvs(2,size = k)
data_next10 = poisson.rvs(2/3, size = k)
data_total40 = poisson.rvs(8/3,size = k)
print(data_first30)

for i in data_first30:
  if i == 0:
    for j in data_next10:
      if j == 1:
        count = count + 1

sec_count = 0
for i in data_total40:
  if i == 1:
    sec_count = sec_count + 1


probab_f = count/(k*k)
probab_b = sec_count/ k
probab = probab_f/probab_b
print(probab)

#plotting
#plotting

cases = ['']

probab_theo = 0.25
probab_sim = probab

#plt.figure(figsize=(24,16))
#plt.subplots_adjust(left = None, bottom = 0, right = None, top = 1, wspace = None, hspace = None )
x = np.arange(len(cases))
plt.bar(x + 0.00, probab_theo, color = 'b', width = 0.2, label = 'Theoretical')
plt.bar(x + 0.2, probab_sim, color = 'g', width = 0.2, label = 'Simulated')
plt.xlabel('Theoretical v/s Simulated')
plt.ylabel('Probability')
plt.xticks(x  + 0.2/2,[''])


a = np.arange(0,0.26,0.001)
plt.yticks(a)
plt.ylim([0.24,0.26])
#plt.margins(0.01)
plt.grid(b = True, color ='black',
        linestyle ='-.', linewidth = 0.5,
        alpha = 0.2)

plt.legend()
plt.show()


