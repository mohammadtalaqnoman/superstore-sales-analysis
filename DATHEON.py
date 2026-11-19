#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[11]:


df = pd.read_csv(r'C:\Users\admin\Downloads\superstore_sales (1).csv')


# In[12]:


print(df.shape)


# In[13]:


print(df.head())


# In[14]:


print(df.isna().sum())


# In[15]:


print(df.duplicated().sum())


# In[16]:


df = df.drop_duplicates()


# In[17]:


df = df.drop(columns=['Row ID'])


# In[18]:


df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')


# In[19]:


df['Ship Date'] = pd.to_datetime(df['Ship Date'], errors='coerce')


# In[20]:


df['Year_Month'] = df['Order Date'].dt.to_period('M')


# In[21]:


df['Year'] = df['Order Date'].dt.year


# In[22]:


df['Month'] = df['Order Date'].dt.month


# In[23]:


df['Profit Margin %'] = df['Profit'] / df['Sales'] * 100


# In[24]:


print(df.shape)


# In[25]:


# 1. Customer Purchase Volume
customer_table = df.groupby('Customer ID')['Sales'].sum().sort_values(ascending=False)


# In[26]:


print(customer_table.head())


# In[27]:


# 2. Monthly Seasonality
monthly_table = df.groupby('Year_Month')[['Sales','Profit']].sum()


# In[28]:


print(monthly_table.tail(12))


# In[29]:


# 3. Category-wise Revenue
category_table = df.groupby('Category')[['Sales','Profit']].sum()


# In[30]:


print(category_table)


# In[31]:


# 4. Discount Sensitivity
discount_table = df.groupby('Discount')[['Sales','Profit']].mean()


# In[32]:


print(discount_table)


# In[33]:


plt.figure(figsize=(10,5))


# In[34]:


sns.barplot(data=df, x='Category', y='Sales', estimator='sum', errorbar=None)


# In[35]:


plt.title('Category Wise Total Sales')


# In[37]:


plt.show()


# In[38]:


monthly_table['Sales'].plot(kind='line', marker='o')


# In[39]:


plt.title('Monthly Seasonality - Sales Up Down')


# In[40]:


plt.show()


# In[41]:


sns.scatterplot(data=df, x='Discount', y='Profit')


# In[42]:


plt.title('Discount Badhao = Profit Ghatao')


# In[ ]:





# In[ ]:




