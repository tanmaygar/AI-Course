import math

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from scipy.stats import norm
from scipy.stats import binom


#number of test cases
k = 100000
#A = (Y = 0 and X3 = 0)
count_A = 0

#B = X3 = 0
count_B = 0

#for loop to move through all test cases
for i in range(k):
  #generate random variable using bernoulli distribution
  data_bern = bernoulli.rvs(size = 3, p=0.5)

  #print(data_bern)
  if data_bern[2] == 0:
    #counting number of times B is coming to be true
    count_B = count_B + 1

  if data_bern[2] == 0 and data_bern[1] * data_bern[0] == 0:
    #counting number of times A is coming to be true
    count_A = count_A + 1

#probability for occurence of A
probab_A = count_A/k

#probability for occurence of B
probab_B = count_B/k

#required conditional probability
probab = probab_A/probab_B
print("The probability is: ", probab)


#plotting
#plotting

cases = ['']

probab_theo = 0.75
probab_sim = probab

#plt.figure(figsize=(24,16))
#plt.subplots_adjust(left = None, bottom = 0, right = None, top = 1, wspace = None, hspace = None )
x = np.arange(len(cases))
plt.bar(x + 0.00, probab_theo, color = 'b', width = 0.2, label = 'Theoretical')
plt.bar(x + 0.2, probab_sim, color = 'g', width = 0.2, label = 'Simulated')
plt.xlabel('Theoretical v/s Simulated')
plt.ylabel('Probability')
plt.xticks(x  + 0.2/2,[''])


a = np.arange(0,0.76,0.001)
plt.yticks(a)
plt.ylim([0.74,0.76])
#plt.margins(0.01)
plt.grid(b = True, color ='black',
        linestyle ='-.', linewidth = 0.5,
        alpha = 0.2)

plt.legend()
plt.show()


