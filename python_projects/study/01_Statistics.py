# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 21:13:12 2018

@author: Balamurugan
"""

""" Central Tendency 
        1.Mean
        2.Median
        3.Mode
"""

import numpy as np
import matplotlib as plt

print('')
print('CENTRAL TENDANCY')
print('----------------')

m = np.random.randint(7,10,20)
print('Data Set : ',m)
print('Mean Calculation   : ',np.mean(m))
print('Median Calculation : ',np.median(m))

from statistics import mode
print('Mode Calculation   : ',mode(m))

""" Population : Total Observations Made
    Sample     : Subset of population selected in  such a way it interprets the population
"""

print('')
print('POPULATION')
print('----------------')
population = np.random.randint(10,20,100)
print('Population : ',population)

print('Mean    : ',np.mean(population))
print('Median  : ',np.median(population))
print('Mode    : ',mode(population))

print('')
print('SAMPLE')
print('----------------')
sample = np.random.choice(population,20)
print('Sample : ',sample)

print('Mean    : ',np.mean(sample))
print('Median  : ',np.median(sample))
print('Mode    : ',mode(sample))

print('')
print('MULTIPLE SAMPLES')
print('----------------')
sample_1 = np.random.choice(population,15)
sample_2 = np.random.choice(population,15)
sample_3 = np.random.choice(population,15)
sample_4 = np.random.choice(population,15)
print('Sample 1 : ',sample_1)
print('Sample 2 : ',sample_2)
print('Sample 3 : ',sample_3)
print('Sample 4 : ',sample_4)
all_samples = [sample,sample_1,sample_2,sample_3,sample_4]
sample_mean = []

for i in all_samples:
    sample_mean.append(np.mean(i))
print('Sample Mean : ',sample_mean)    

print('Mean of Multiple Samples : ',np.mean(sample_mean))  
print('Mean of Population       : ',np.mean(population))    


""" Measure of Spread : Gives the variability in the data and how well it is distributed
         1.Range
               How well the data is spread out (Low and High value and the difference is taken)
         2.Quartile
               Splits the dataset into multiple take the median of each and 
               calculate the inter quartile range
         3.Variance
               How far the data is from the mean, changes for popuation and sample
         4.Standard Deviation
               Square root of variance - More exact than Variance
"""
print('')
print('MEASURE OF SPREAD')
print('-----------------')
print('')
print('RANGE CALCULATION')
print('')
n = np.random.randn(30)
print('Array of Numbers : ',n)
print('Maximum Value    : ',np.max(n))
print('Minimum Value    : ',np.min(n))
print('Range(Max - Min) : ',np.max(n) - np.min(n))
print('')
print('QUARTILE CALCULATION')
print('')
Q1 = np.percentile(n,25)
Q2 = np.percentile(n,50)
Q3 = np.percentile(n,75)
print('First Quartile : ',Q1)
print('Second Quartile: ',Q2)
print('Third Quartile : ',Q3)
print('Inter Quartile Range(Third-First) : ',Q3 - Q1)
print('')
print('VARIANCE CALCULATION')
print('')
population = np.random.rand(100)
sample = np.random.choice(population,30)
print('Population : ',population)
print('Sample     : ',sample)
print('Variance of Population       : ',np.var(population))
print('Variance of Sample           : ',np.var(sample))
print('Sqrt(Variance) of Population : ',np.sqrt(np.var(population)))
print('Sqrt(Variance) of Sample     : ',np.sqrt(np.var(sample)))
print('')
print('STANDARD DEVIATION CALCULATION')
print('')
print('Standard Deviation of Population : ',np.std(population))
print('Standard Deviation of Sample     : ',np.std(sample))















