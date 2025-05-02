import pandas as pd

dict1 ={'Name':['Priyang','Aadhya','Krisha','Vedant','Parshv',
                'Mittal','Archana'],
                'Marks':[98,89,99,87,90,83,99],
                'Gender':['Male','Female','Female','Male','Male',
                         'Female','Female']
               }
df1=pd.DataFrame(dict1)
df1


#Find top 3 rows of dataset
df1.head(3)

#find the last 3 rows of dataset
df1.tail(3)

#find shape of the dataset(number of rows and columns)
df1.shape  # shape is not a method it is an attribute

print('Number of rows', df1.shape[0])
print('Number of columns', df1.shape[1])

# get info about the dataset
df1.info()

# check null values in the dataset
df1.isnull()
df1.isnull().sum()

# get overall statistics about the dataframe
df1.describe() #by default only applicable for numeric columns

df1.describe(include='all') # for all columns

#find the unique values from gender column
df1['Gender'].unique()

#find the number of unique values
df1['Gender'].nunique()

# display the count of unique values in gender column
df1['Gender'].value_counts()

#Find the total number of students having marks between 90 to 100

#method 1
len(df1[(df1['Marks']>=90) & (df1['Marks']<=100)])

#method 2
(df1['Marks'].between(90,100))
sum((df1['Marks'].between(90,100)))

#Find average marks
df1['Marks'].mean()
df1['Marks'].max()
df1['Marks'].min()

#apply method
def marks(x):
    return x//2

df1['Half_marks']=df1['Marks'].apply(marks)
df1

# lambda method
df1['Marks'].apply(lambda x:x/2)

# Find length of the names using apply method
df1['Name'].apply(len)

# Map function
df1['Gender'].map({'Male':1, 'Female':0})
df1['Male_Female_Code'] = df1['Gender'].map({'Male':1, 'Female':0})
df1

# Drop the columns
df1.drop(['Half_marks','Male_Female_Code'], axis=1, inplace=True)
df1

# print name of the columns
df1.columns

# sort the dataframe as per the marks column
df1.sort_values(by=['Marks','Gender'], ascending=False)

# Display name and marks of female students
df1[df1['Gender']=='Female'] [['Name', 'Marks']]

df1[df1['Gender'].isin(['Female'])] [['Name','Marks']]

