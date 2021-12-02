#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import random 
import matplotlib.pyplot as plt
import scipy.stats as st
import statsmodels.api as sm
import pandas as pd


# In[2]:


def generating_random_samples(n):
    x_values = []
    y_values =[] 
    for i in range(10000):    
        x_values.append(np.random.uniform(0, 1, n)) 
        y_values.append(np.random.uniform(0, 1, n)) 
    return x_values, y_values


# In[3]:


# def calculating_correlation_coefficients(x, y):
#     corr = np.corrcoef(x, y)
#     print(len(corr)) 
#     return corr

def calculating_correlation_coefficients(x, y):
    corr = []
    for i in range(len(x)):
        corr.append(np.corrcoef(x[i], y[i])[0][1]) 
    return corr


# In[4]:


# 1. Plot the distribution of 10000 correlations.

def plot_the_distribution(corr):
    plt.figure(figsize = (12, 9))
    plt.hist(corr, bins = 100, color = "blue", ec = "purple")
    plt.title('Sampling distribution of correlations');


# In[5]:


# 2. Using QQ plots check if the distribution is normal or not.

def qqplot(corr):
    a = pd.Series(corr)
    sm.qqplot(a, line ='q', dist = st.norm)
    plt.show();


# In[6]:


# 3. What is the probability that you would get a correlation that is larger than 0.3 or smaller than -0.3?
           # a. Calculate the probability based on the histogram

def calculate_the_probability_a(corr):
    count = 0
    for i in corr:
        if i <= -0.3 or i >= 0.3:
            count += 1
    print(f' Probability that is larger than 0.3 or smaller than -0.3(histogram) = {(count/len(corr))}')


# In[8]:


# 3. What is the probability that you would get a correlation that is larger than 0.3 or smaller than -0.3?
           # b. Calculate the probability assuming the distribution is normal 
           # (Hint: standardize the correlation coefficients and use the Z table to calculate the probabilities)

def calculate_the_probability_b(corr):
    mean = np.mean(corr)
    std = np.std(corr) 
    print(f' mean = {mean} \n std = {std}')
    
    value1 = st.norm.cdf(-0.3, mean, std)
    value2 = 1 - st.norm.cdf(0.3, mean, std)
    
    min = st.norm.cdf(np.min(corr), mean, std)
    max = 1 - st.norm.cdf(np.max(corr), mean, std)
    
    if min < value1:
        z_value1 = value1 - min
    else:
        z_value1 = value1
    if max < value2:
        z_value2 = value2 - max
    else:
        z_value2 = value2
    z_value = z_value1 + z_value2
    
    print(f' Probability that is larger than 0.3 or smaller than -0.3(Z table) = {z_value}')


# In[9]:


# 4. What are 5% and 95% percentiles? What are 2.5% and 97.5% percentiles?

def percentiles(corr):
    p1 = np.percentile(corr, 95)
    p2 = np.percentile(corr, 5)
    p3 = np.percentile(corr, 97.5)
    p4 = np.percentile(corr, 2.5)
    print(f' 95% percentile = {p1},  5% percentile = {p2}, \n 97.5% percentile = {p3},  2.5% percentile = {p4}')


# In[10]:


# 5. Change the sample size from 20 to 10 and perform the steps from 1 to 4. Try the following sample sizes too: 50, 100, 1000.

# n = 20
x, y = generating_random_samples(20)
corr = calculating_correlation_coefficients(x, y)

plot_the_distribution(corr)

qqplot(corr)

calculate_the_probability_a(corr)
calculate_the_probability_b(corr)

percentiles(corr)


# In[11]:


# QQ plot-ից մենք կարող ենք տեսնել, որ մեր distribution-ը մոտավորապես normal է։


# In[12]:


# n = 10
x, y = generating_random_samples(10)
corr = calculating_correlation_coefficients(x, y)

plot_the_distribution(corr)

qqplot(corr)

calculate_the_probability_a(corr)
calculate_the_probability_b(corr)

percentiles(corr)


# In[13]:


# n = 50
x, y = generating_random_samples(50)
corr = calculating_correlation_coefficients(x, y)

plot_the_distribution(corr)

qqplot(corr)

calculate_the_probability_a(corr)
calculate_the_probability_b(corr)

percentiles(corr)


# In[14]:


# n = 100
x, y = generating_random_samples(100)
corr = calculating_correlation_coefficients(x, y)

plot_the_distribution(corr)

qqplot(corr)

calculate_the_probability_a(corr)
calculate_the_probability_b(corr)

percentiles(corr)


# In[15]:


# n = 1000
x, y = generating_random_samples(1000)
corr = calculating_correlation_coefficients(x, y)

plot_the_distribution(corr)

qqplot(corr)

calculate_the_probability_a(corr)
calculate_the_probability_b(corr)

percentiles(corr)


# In[16]:


# n = 10000
x, y = generating_random_samples(10000)
corr = calculating_correlation_coefficients(x, y)

plot_the_distribution(corr)

qqplot(corr)

calculate_the_probability_a(corr)
calculate_the_probability_b(corr)

percentiles(corr)


# In[17]:


# Ինչքան մեծացնում ենք n-ը correlation-ի արժեքների -0.3-ից փոքր և 0.3-ից մեծ լինելու հավանականությունը փոքրանում է,
        # այսինքն correlation-ի արժեքների միջակայքը փոքրանում է։
# Ինչքան մեծացնում ենք n-ը variance-ը փոքրանում է, այսինքն այն ավելի է ձգտում normal-ի: Սա կարելի է տեսնել նաև QQ plot-ից։

