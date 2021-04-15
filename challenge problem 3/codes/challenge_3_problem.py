import math

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from scipy.stats import norm
from scipy.stats import binom
from scipy.stats import poisson
from scipy.stats import uniform

#number of test cases
k = 100000
count = 0
data_variable = uniform.rvs(0,10, size=4)
for i in range(k):
  data_variable = uniform.rvs(0,10,size = 4)
 # print(data_variable)
  if data_variable[0] > data_variable[1]:
    if data_variable[1] > data_variable[2]:
      if data_variable[2] > data_variable[3]:
        count = count + 1

probab=count/k
print(probab)

#plotting
#plotting

cases = ['']

probab_theo = 1/24
probab_sim = probab

#plt.figure(figsize=(24,16))
#plt.subplots_adjust(left = None, bottom = 0, right = None, top = 1, wspace = None, hspace = None )
x = np.arange(len(cases))
plt.bar(x + 0.00, probab_theo, color = 'b', width = 0.2, label = 'Theoretical')
plt.bar(x + 0.2, probab_sim, color = 'g', width = 0.2, label = 'Simulated')
plt.xlabel('Theoretical v/s Simulated')
plt.ylabel('Probability')
plt.xticks(x  + 0.2/2,[''])


a = np.arange(0,0.05,0.0001)
plt.yticks(a)
plt.ylim([0.04,0.043])
#plt.margins(0.01)
plt.grid(b = True, color ='black',
        linestyle ='-.', linewidth = 0.5,
        alpha = 0.2)

plt.legend()
plt.show()


