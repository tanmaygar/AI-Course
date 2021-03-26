#assignment 3

import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from scipy.stats import norm
from scipy.stats import binom
from scipy.stats import semicircular

#number of test cases for each variable
k = 10000

#counter for counting the number of times favourable situation occurs
count = 0
#creating an array of x coordinate using semicircular function
data_x = semicircular.rvs(loc = 0, scale = 1, size = k, random_state = None)

#creating an array of x coordinate using semicircular function
data_y = semicircular.rvs(loc = 0, scale = 1, size = k, random_state = None)

#comparing each term of both arrays and counting number of times the favourable situation occurs
for i in range(k):
  for j in range(k):
    #print(" " + str(data_y[j]) + ":" + str(data_x[i]))
    if (data_y[j] > abs(data_x[i])):
      count = count + 1

#probability of the event is number of times the situation occured / total test cases
# total test cases is k^2
probab = count/pow(k,2)
print("The probability is: ", probab)

#plotting

cases = ['']

probab_theo = 0.25
probab_sim = probab

x = np.arange(len(cases))
plt.bar(x + 0.00, probab_theo, color = 'b', width = 0.2, label = 'Theoretical')
plt.bar(x + 0.2, probab_sim, color = 'g', width = 0.2, label = 'Simulated')
plt.xlabel('Theoretical v/s Simulated')
plt.ylabel('Probability')
plt.xticks(x  + 0.2/2,[''])
a = np.arange(0,0.3,0.01)
plt.yticks(a,a)
plt.margins(0.05)
plt.grid(b = True, color ='black',
        linestyle ='-.', linewidth = 0.5,
        alpha = 0.2)
plt.legend()
plt.show()