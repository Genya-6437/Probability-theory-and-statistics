#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import scipy.stats as st


# In[9]:


# 6.Plot QQ plot yourself
# a.X - axis: standard normal distribution

np_normal = pd.Series(np.random.normal(0, 1, 1000))

fig = sm.qqplot(np_normal,line='q',dist=st.norm)
plt.show()


# In[12]:


# b.Y - axis: binomial distribution with some parameters

np_binomial = pd.Series(np.random.binomial(100, 0.2, 1000))

fig = sm.qqplot(np_binomial,line='q',dist=st.norm)
plt.show()


# In[24]:


# 7.Try different distributions and see how the plot changes (right/left skewed, uniform, etc.).

x = np.linspace(-5, 5, 10000)


# In[25]:


y_norm = st.norm.pdf(x_values)

plt.figure(figsize = (10, 7))
plt.plot(x, y_norm);


# In[40]:


y_norm_cdf = st.norm.cdf(x)

plt.figure(figsize = (10, 7))
plt.plot(x, y_norm_cdf);


# In[22]:


y_skew_left = st.skewnorm.pdf(x_values, -1)

plt.figure(figsize = (10, 7))
plt.plot(x, y_skew_left);


# In[41]:


y_skew_left_cdf = st.skewnorm.cdf(x, -1)

plt.figure(figsize = (10, 7))
plt.plot(x, y_skew_left_cdf);


# In[26]:


y_skew_right = st.skewnorm.pdf(x_values, 1)

plt.figure(figsize = (10, 7))
plt.plot(x, y_skew_right);


# In[42]:


y_skew_right_cdf = st.skewnorm.cdf(x, 1)

plt.figure(figsize = (10, 7))
plt.plot(x, y_skew_right_cdf);


# In[30]:


y_uniform = st.uniform.pdf(x)

plt.figure(figsize = (10, 7))
plt.plot(x, y_uniform);


# In[43]:


y_uniform_cdf = st.uniform.cdf(x)

plt.figure(figsize = (10, 7))
plt.plot(x, y_uniform_cdf);


# In[34]:


y_binom = st.binom.pmf(x, 5, 0.4)

plt.figure(figsize = (10, 7))
plt.plot(x, y_binom);


# In[44]:


y_binom_cdf = st.binom.cdf(x, 5, 0.4)

plt.figure(figsize = (10, 7))
plt.plot(x, y_binom_cdf);


# In[38]:


y_expon = st.expon.pdf(x)

plt.figure(figsize = (10, 7))
plt.plot(x, y_expon);


# In[45]:


y_expon_cdf = st.expon.cdf(x)

plt.figure(figsize = (10, 7))
plt.plot(x, y_expon_cdf);


# In[54]:


y_bernoulli = st.bernoulli.pmf(x, 0.4)

plt.figure(figsize = (10, 7))
plt.plot(x, y_bernoulli);


# In[56]:


y_bernoulli_cdf = st.bernoulli.cdf(x, 0.4)

plt.figure(figsize = (10, 7))
plt.plot(x, y_bernoulli_cdf);


# In[47]:


y_poisson = st.poisson.pmf(x, 0.6)

plt.figure(figsize = (10, 7))
plt.plot(x, y_poisson);


# In[51]:


y_poisson_cdf = st.poisson.cdf(x, 0.6)

plt.figure(figsize = (10, 7))
plt.plot(x, y_poisson_cdf);


# In[ ]:




