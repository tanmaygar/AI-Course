import math

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from scipy.stats import norm
from scipy.stats import binom


#number of test cases
k = 10000
probab_knows = 2/3
probab_guess = 1/4

student_knowing_trial = bernoulli.rvs(size = k, p = probab_knows)

student_guessing_trial = bernoulli.rvs(size = k, p = probab_guess)

correct_A = 0
correct_B = 0
knowing = 0

for i in student_knowing_trial:
  if i == 1:
    correct_A = correct_A + 1
    knowing = knowing + 1
  
  if i == 0:
    for j in student_guessing_trial:
      if j == 1:
        correct_B = correct_B + 1

knowing_probab = knowing/(k)
correct_probab = correct_A/k + correct_B/(k*k)
#print(knowing_probab)
#print(correct_probab)
probab = knowing_probab/correct_probab
print("The probability is: ", probab)
#print(8/9)

#plotting
#plotting

cases = ['']

probab_theo = 8/9
probab_sim = probab

#plt.figure(figsize=(24,16))
#plt.subplots_adjust(left = None, bottom = 0, right = None, top = 1, wspace = None, hspace = None )
x = np.arange(len(cases))
plt.bar(x + 0.00, probab_theo, color = 'b', width = 0.2, label = 'Theoretical')
plt.bar(x + 0.2, probab_sim, color = 'g', width = 0.2, label = 'Simulated')
plt.xlabel('Theoretical v/s Simulated')
plt.ylabel('Probability')
plt.xticks(x  + 0.2/2,[''])


a = np.arange(0,0.9,0.001)
plt.yticks(a)
plt.ylim([0.87,0.9])
#plt.margins(0.01)
plt.grid(b = True, color ='black',
        linestyle ='-.', linewidth = 0.5,
        alpha = 0.2)

plt.legend()
plt.show()
