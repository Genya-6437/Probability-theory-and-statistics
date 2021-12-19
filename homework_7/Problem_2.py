#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import random 


# In[2]:


x_values = np.random.uniform(8, 10, 5)


# In[3]:


print(x_values)


# In[4]:


data = np.array(x_values)

q3, q1 = np.percentile(data, [75 ,25])
iqr = q3 - q1

print('The Interquartile Range for the data is:',iqr)


# In[15]:


def Interquartile_Range(n):
    iqr = []
    for i in range(3):
        x_values = np.random.uniform(8, 10, n)   
        data = np.array(x_values)
        q3, q1 = np.percentile(data, [75 ,25])
        iqr.append(q3 - q1)
    
    return np.mean(iqr)
    


# In[16]:


print('The Interquartile Range for the data when n=5 is:', Interquartile_Range(5))
print('The Interquartile Range for the data when n=10 is:', Interquartile_Range(10))
print('The Interquartile Range for the data when n=20 is:', Interquartile_Range(20))
print('The Interquartile Range for the data when n=30 is:', Interquartile_Range(30))


# In[ ]:




