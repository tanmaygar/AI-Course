#challeneg question mixture

import math

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from scipy.stats import norm
from scipy.stats import binom
from scipy.stats import poisson
from scipy.stats import uniform

#number of test cases
k = 5000
count_1 = 0
count_2 = 0

data_x = binom.rvs(n=5, p = 0.5, size = k)
data_y = uniform.rvs(0,1,size = k)

for x in data_x:
  for y in data_y:
    if x + y <=2:
      count_1 = count_1 + 1
    if x+y >=5:
      count_2 = count_2 + 1

probab_1 = count_1/(k*k)
probab_2 = count_2/(k*k)

probab = probab_1/probab_2
print(probab)


#plotting
#plotting

cases = ['']

probab_theo = 6
probab_sim = probab

#plt.figure(figsize=(24,16))
#plt.subplots_adjust(left = None, bottom = 0, right = None, top = 1, wspace = None, hspace = None )
x = np.arange(len(cases))
plt.bar(x + 0.00, probab_theo, color = 'b', width = 0.2, label = 'Theoretical')
plt.bar(x + 0.2, probab_sim, color = 'g', width = 0.2, label = 'Simulated')
plt.xlabel('Theoretical v/s Simulated')
plt.ylabel('Probability')
plt.xticks(x  + 0.2/2,[''])


a = np.arange(0,6.5,0.1)
plt.yticks(a)
plt.ylim([5.5,6.5])
#plt.margins(0.01)
plt.grid(b = True, color ='black',
        linestyle ='-.', linewidth = 0.5,
        alpha = 0.2)

plt.legend()
plt.show()

