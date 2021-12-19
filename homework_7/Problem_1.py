#!/usr/bin/env python
# coding: utf-8

# In[51]:


import numpy as np
import matplotlib.pyplot as plt


# In[50]:


# 1. Determine the sampling distribution of X_mean, calculate E(X_mean), and compare to .

X = [25, 40, 65]
P = [0.2, 0.5, 0.3]


# In[28]:


sample_mean = []
sample_var = []
probability = []

for i in X:
    for j in X:
        mean = np.mean([i,j])
        sample_mean.append(mean)
        sample_var.append(pow((i-mean), 2) + pow((j-mean), 2))
        p = P[X.index(i)] * P[X.index(j)]
        probability.append(p)


# In[ ]:


# plt.figure(figsize = (12,9))
# plt.hist(sample_mean, 15);


# In[34]:


def expected_value(x, p):
    E_x = 0
    for i in range(len(x)):
        E_x += x[i] * p[i]
    return E_x
    
print("Expected value of sample_mean = ", expected_value(sample_mean, probability))
print("Expected value of X = ", expected_value(X, P))


# In[54]:


# 2. Determine the sampling distribution of the sample variance S^2, calculate E(S^2), and compare to sigma^2.

# plt.figure(figsize = (12,9))
# plt.hist(sample_var, 15);


# In[38]:


X_2 = [i*i for i in X]

E_x_2 = expected_value(X_2, P)
E_x = expected_value(X, P)

print("Variance of sample_variance = ", expected_value(sample_var, probability))
print("Variance of X = ", E_x_2 - E_x*E_x)

