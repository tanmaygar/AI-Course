import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from scipy.stats import norm
from scipy.stats import binom


#function to calculate factorial
def fact_func(a):
  ans = 1
  for x in range(1 , a + 1):
    ans = ans * x
  return ans

#function to calculate binomial coefficient
def ncr(n , r):
  ans = fact_func(n) / (fact_func(r) * fact_func(n - r))
  return ans

#function to calculate the probability 
def probab_func(n , p , q , a , b):
  sum = 0
  for x in range(a , b + 1):
    sum = sum + ( ncr(n , x) )* ( pow(p , x) ) * ( pow(q , n - x) )
  return sum

n = 6
p = 2 / 5
q = 3 / 5
print("The probability that all will bear X is: " , probab_func(n , p , q , 6 , 6))
print("The probability that not more than 2 will bear 'Y' mark is: " , probab_func(n , p , q , 4 , 6))
print("The probability that at least one ball will bear 'Y' mark is: " , probab_func(n , p , q , 0 , 5))
print("The probability that the number of balls with 'X' mark and 'Y' mark will be equal is: " , probab_func(n , p , q , 3 , 3))

#imported numpy for making binomial distribution

num_trails = 1000000
sample_space = np.random.binomial(n , p , num_trails)
#print("Some number this is " , sample_space)
count = 0
for i in sample_space:
  if i == 6:
    count = count + 1

probability_check = count / num_trails
print("The probability that all will bear X is: " , probability_check)

count = 0
for i in sample_space:
  if i == 3:
    count = count + 1
probability_check = count / num_trails
print("The probability that the number of balls with 'X' mark and 'Y' mark will be equal is: " , probability_check)

count = 0
for i in sample_space:
  if i == 4 or i == 5 or i == 6:
    count = count + 1
probability_check = count / num_trails
print("The probability that not more than 2 will bear 'Y' mark is: " , probability_check)

count = 0
for i in sample_space:
  if i != 6:
    count = count + 1
probability_check = count / num_trails
print("The probability that at least one ball will bear 'Y' mark is: " , probability_check)
