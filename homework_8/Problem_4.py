#!/usr/bin/env python
# coding: utf-8

# In[19]:


import numpy as np
import math
import scipy.stats as st


# In[33]:


mean = 11.5
std = 4.0


# In[34]:


# 1.In a sample of 50 randomly selected customers, what is the approximate probability that the sample mean amount purchased is at least 12 gallons?
n = 50
x_mean = 12

P_1 = round(st.norm.cdf(round((x_mean - mean)/(std / math.sqrt(n)), 2)), 4)

print(f'P(x_mean > 12) = 1 - P(x_mean < 12) = {1 - P_1}')


# In[35]:


# 2. In a sample of 50 randomly selected customers, what is the approximate probability that the total amount of gasoline purchased is at most 600 gallons?
n = 50
sum_x = 600

P_2 = round(st.norm.cdf(round((sum_x - n * mean)/(std * math.sqrt(n)), 2)), 4)

print(f'P(sum_x < 600) = {P_2}')


# In[39]:


# 3. What is the approximate value of the 95th percentile for the total amount purchased by 50 randomly selected customers?
n = 50
percentile = 0.95
y = round(round(st.norm.ppf(percentile), 2) * std * math.sqrt(n) + n * mean)

print(f'The approximate value of the 95th percentile = {y}')

