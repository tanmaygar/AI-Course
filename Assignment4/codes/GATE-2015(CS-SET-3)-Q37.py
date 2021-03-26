import math

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from scipy.stats import norm
from scipy.stats import binom


k = 100000
count_A = 0
count_B=0
for i in range(k):
  data_bern = bernoulli.rvs(size = 3, p=0.5)
  #print(data_bern)
  if data_bern[2] == 0:
    count_B = count_B + 1
  if data_bern[2] == 0 and data_bern[1] * data_bern[0] == 0:
    count_A = count_A + 1

probab_A = count_A/k
probab_B = count_B/k
probab = probab_A/probab_B
print("The probability is: ", probab)


#plotting

cases = ['']

probab_theo = 0.75
probab_sim = probab

x = np.arange(len(cases))
plt.bar(x + 0.00, probab_theo, color = 'b', width = 0.2, label = 'Theoretical')
plt.bar(x + 0.2, probab_sim, color = 'g', width = 0.2, label = 'Simulated')
plt.xlabel('Theoretical v/s Simulated')
plt.ylabel('Probability')
plt.xticks(x  + 0.2/2,[''])
plt.legend()
plt.show()