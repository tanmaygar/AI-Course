import math

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from scipy.stats import norm
from scipy.stats import binom


#number of test cases
k = 100000

#probab for first pick king
probab_A = 4/52

#probab for second pick king given A
probab_B = 3/51

#total 
count = 0

#count_A = 0

#bernoulli trials for picking first card
first_round_trails = bernoulli.rvs(size = k, p = probab_A)

#bernoulli trials for picking second card given first is king
second_round_trails = bernoulli.rvs(size = k, p = probab_B)


for i in first_round_trails:
  if i == 1:
    #count_A = count_A + 1
    for j in second_round_trails:
      if j == 1:
        count = count + 1


probab = count/(k*k)
print("The probability for both cards to be king without replacement: ", probab)
#print(probab_A *3/51)




#plotting
#plotting

cases = ['']

probab_theo = probab_A * probab_B
probab_sim = probab

#plt.figure(figsize=(24,16))
#plt.subplots_adjust(left = None, bottom = 0, right = None, top = 1, wspace = None, hspace = None )
x = np.arange(len(cases))
plt.bar(x + 0.00, probab_theo, color = 'b', width = 0.2, label = 'Theoretical')
plt.bar(x + 0.2, probab_sim, color = 'g', width = 0.2, label = 'Simulated')
plt.xlabel('Theoretical v/s Simulated')
plt.ylabel('Probability')
plt.xticks(x  + 0.2/2,[''])


a = np.arange(0,0.006,0.0001)
plt.yticks(a)
plt.ylim([0.004,0.005])
#plt.margins(0.01)
plt.grid(b = True, color ='black',
        linestyle ='-.', linewidth = 0.5,
        alpha = 0.2)

plt.legend()
plt.show()


