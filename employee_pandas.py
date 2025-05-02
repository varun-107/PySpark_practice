#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
df = pd.read_csv('Salaries.csv')


# In[ ]:


# find shape of the dataset
df.shape # .shape is an attribute


# In[ ]:


df.info()


# In[ ]:


# check null values in the dataset
df.isnull() # it returns a boolean table
df.isnull().sum()


# In[ ]:


# drop notes agency and status columns
df = df.drop(['Notes','Agency','Status'],axis=1)


# In[ ]:


# get overall stats of the dataset
df.describe() # only for numerical columns
df.describe(include='all')


# In[ ]:


# Find occurence of the employee names
df['EmployeeName'].value_counts().head(5)


# In[ ]:


# Find unique job titles
df['JobTitle'].nunique()


# In[ ]:


# total number of job titles 'captain'
df[df['JobTitle'].str.contains('captain',case=False)]
x = len(df[df['JobTitle'].str.contains('captain',case=False)])
print(f"Total number of captains are {x}")


# In[ ]:


#display all the emp names from fire department
df[df['JobTitle'].str.contains('Fire',case=False)] ['EmployeeName']


# In[ ]:


# min, max and average base pay
df.columns
df['BasePay'].describe()


# In[ ]:


# Replace 'Not Provided' in EmployeeName column to NaN
df['EmployeeName'].replace('Not provided',np.nan)


# In[ ]:


# drop the rows having 5 missing values
df.drop(df[df.isnull().sum(axis=1)==5].index,axis=0,inplace=True)

