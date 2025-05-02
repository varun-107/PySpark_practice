#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd


# In[ ]:


df = pd.read_csv('Ecommerce Purchases')


# In[ ]:


# check first 10 rows of the dataset
df.head(10)

# check last 10 rows of the dataset
# df.tail(10)


# In[ ]:


# check datatype of each column
df.dtypes  #attribute


# In[ ]:


#check null values in the dataset
df.isnull().sum()


# In[ ]:


#How many rows and columns are there in the dataset
df.columns  # attribute

no_of_columns = len(df.columns)
no_of_rows = len(df)

print(f"no of rows: {no_of_rows} \nno of columns: {no_of_columns}")


# In[ ]:


# highest and lowest purchase price
df.columns
max_price = df['Purchase Price'].max()
mini_price = df['Purchase Price'].min()

print(f"max purchase price: {max_price} \nmin purchase price: {mini_price}")


# In[ ]:


# average purchase price
df['Purchase Price'].mean()


# In[ ]:


# How many people have French 'fr' as their language
df.columns
df[df['Language']=='fr']
len(df[df['Language']=='fr'])


# In[ ]:


df[df['Language']=='fr'].count() 


# In[ ]:


# job title contains engineer
df.columns
df[df['Job'].str.contains('engineer')]  # by default case sensitive
df[df['Job'].str.contains('engineer',case=False)] # case insensituve search
x = len(df[df['Job'].str.contains('engineer',case=False)])
print(f"no of engineers: {x}")


# In[ ]:


# Find the email of the person with the IP address: 132.207.160.22
df['IP Address']=='132.207.160.22' #boolean array
df[df['IP Address']=='132.207.160.22']['Email']


# In[ ]:


# How many people have mastercard as their credit card provider and made a purchase above 50
df.columns
df[(df['CC Provider']=='Mastercard') & (df['Purchase Price'] > 50)]
x = len(df[(df['CC Provider']=='Mastercard') & (df['Purchase Price'] > 50)])
print(f"{x} people have mstercard and made a purchase above 50")


# In[ ]:


# How many people purchase during AM and how many people purchase during PM ?
df['AM or PM'].value_counts()


# In[ ]:


# How many people have a credit card that expires in 2020
df.columns


# In[ ]:


df['CC Exp Date']


# In[ ]:


def fun():
    count=0
    for date in df['CC Exp Date']:
        if date.split('/')[1]=='20':
            count+=1
    print(count)


# In[ ]:


fun()


# In[ ]:


#using lambda function
len(df[df['CC Exp Date'].apply(lambda x:x[3:]=='20')])


# In[ ]:


# Top 5 most popular Email providers
list1=[]
for email in df['Email']:
    list1.append(email.split('@')[1])

df['temp']=list1
df['temp'].value_counts().head(5)


# In[ ]:


# using lambda function
df['Email'].apply(lambda x: x.split('@')[1]).value_counts().head(5)

