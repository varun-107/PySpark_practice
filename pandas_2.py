import pandas as pd

df = pd.read_csv('Ecommerce Purchases')

# check first 10 rows of the dataset
df.head(10)

# check last 10 rows of the dataset
df.tail(10)

# check datatype of each column
df.dtypes  #attribute

#check null values in the dataset
df.isnull().sum()

#How many rows and columns are there in the dataset
df.columns  # attribute

no_of_columns = len(df.columns)
no_of_rows = len(df)

print(f"no of rows: {no_of_rows} \nno of columns: {no_of_columns}")

# highest and lowest purchase price
df.columns
max_price = df['Purchase Price'].max()
mini_price = df['Purchase Price'].min()

print(f"max purchase price: {max_price} \nmin purchase price: {mini_price}")

# average purchase price
df['Purchase Price'].mean()

# How many people have French 'fr' as their language
df.columns
df[df['Language']=='fr']
len(df[df['Language']=='fr'])

df[df['Language']=='fr'].count() 

# job title contains engineer
df.columns
df[df['Job'].str.contains('engineer')]  # by default case sensitive
df[df['Job'].str.contains('engineer',case=False)] # case insensituve search
x = len(df[df['Job'].str.contains('engineer',case=False)])
print(f"no of engineers: {x}")

# Find the email of the person with the IP address: 132.207.160.22
df['IP Address']=='132.207.160.22' #boolean array
df[df['IP Address']=='132.207.160.22']['Email']

# How many people have mastercard as their credit card provider and made a purchase above 50
df.columns
df[(df['CC Provider']=='Mastercard') & (df['Purchase Price'] > 50)]
x = len(df[(df['CC Provider']=='Mastercard') & (df['Purchase Price'] > 50)])
print(f"{x} people have mstercard and made a purchase above 50")

# How many people purchase during AM and how many people purchase during PM ?
df['AM or PM'].value_counts()

# How many people have a credit card that expires in 2020
df.columns

df['CC Exp Date']

def fun():
    count=0
    for date in df['CC Exp Date']:
        if date.split('/')[1]=='20':
            count+=1
    print(count)

fun()

#using lambda function
len(df[df['CC Exp Date'].apply(lambda x:x[3:]=='20')])

# Top 5 most popular Email providers
list1=[]
for email in df['Email']:
    list1.append(email.split('@')[1])

df['temp']=list1
df['temp'].value_counts().head(5)

# using lambda function
df['Email'].apply(lambda x: x.split('@')[1]).value_counts().head(5)

