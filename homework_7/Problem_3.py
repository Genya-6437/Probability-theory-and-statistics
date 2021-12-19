#!/usr/bin/env python
# coding: utf-8

# In[28]:


import numpy as np
import random 
import matplotlib.pyplot as plt
import scipy.stats as st


# In[16]:


def sampling_distribution(mean, sigma, size):
    sample_mean = []
    for i in range(1000):
        x_values = np.random.lognormal(mean, sigma, size)
        sample_mean.append(np.mean(x_values))
    return sample_mean


# In[18]:


mean = 3
sigma = 1


# In[31]:


plt.figure(figsize = (10,7))
plt.hist(sampling_distribution(mean, sigma, 10), 15);


# In[19]:


plt.figure(figsize = (10,7))
plt.hist(sampling_distribution(mean, sigma, 20), 15);


# In[21]:


plt.figure(figsize = (10,7))
plt.hist(sampling_distribution(mean, sigma, 30), 15);


# In[22]:


plt.figure(figsize = (10,7))
plt.hist(sampling_distribution(mean, sigma, 50), 15);


# In[ ]:


# Բոլորի դեպքում էլ sampling distribution-ը նման է նորմալին։

