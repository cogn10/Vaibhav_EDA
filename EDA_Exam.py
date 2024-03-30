#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 1 Import all the necessary libraries for performing mentioned objectives on the Given dataset
# 2 Load the dataset from the given location.
# 3 Plot Histogram for the specified data
# 4 Plot the bar chart for the specified data
# 5 Create a Correlation Matrix
# 6 Plot heat map for the specified data
# 6 Find the column with the most number of missing values
# 7 Impute the data in the given column according to the given specification
# 8 Convert the negative value of the column to positive values
# 10 Plot Box Plot for the specified data.
# 11.Apply Standardization of the data


# In[31]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

file_location="D:\\data_Science\\Data_For_Working\\Telecom.csv"
telecom_DF = pd.read_csv(file_location)

telecom_DF
telecom_DF.columns
telecom_DF.dtypes

#telecom_DF['Customer Status'].value_counts().plot.bar()



plt.subplot(221)
telecom_DF['Gender'].value_counts(normalize=True).plot.bar(figsize=(24,6),title='Gender')
plt.subplot(222)
telecom_DF['Married'].value_counts(normalize=True).plot.bar(figsize=(24,6),title='Married')
plt.subplot(223)
telecom_DF['Multiple Lines'].value_counts(normalize=True).plot.bar(figsize=(24,6),title='MultipleLines')
plt.subplot(224)
telecom_DF['Internet Service'].value_counts(normalize=True).plot.bar(figsize=(24,6),title='InternetService')
plt.show()

## 1) Male and Female both are same users (50 - 50 % same users)
## 2) 55 % are users is non Married and 45 % users is Married.
## 3) 80 % users is use Internet services and 20 % users not using Internet.


# In[32]:


plt.subplot(131)
telecom_DF['Internet Type'].value_counts(normalize=True).plot.bar(figsize=(24,6),title='InternetType')
plt.subplot(132)
telecom_DF['Contract'].value_counts(normalize=True).plot.bar(figsize=(24,6),title='Contract')
plt.subplot(133)
telecom_DF['Customer Status'].value_counts(normalize=True).plot.bar(figsize=(24,6),title='Customer Status')
plt.show()

# *** Internet Type
# 1) 55% users use Fiber Optics 
# 2) 30 % users use DSL
# 3) 15 % users use via Cable

# **** Customer Status
# 1) 65% stayed in same network and 5 % joined the network
# 2) around 30 % customer need to Churned.

# **** Contract
#1) 50 % customer subscription is month to month. 
#2) 28 % Customer subscription is on one year.
#3) 22 % Customer subscription is on one year.


# In[34]:


plt.subplot(121) 
sns.distplot(telecom_DF['Total Revenue'])
plt.subplot(122) 
telecom_DF['Total Revenue'].plot.box(figsize=(16,5)) 

plt.show()


# In[41]:


city_count=dict(telecom_DF['City'].value_counts())
city_count

# Online Security
# Online Backup
# Device Protection Plan
# Premium Tech Support
# Streaming TV
# Streaming Movies
# Streaming Music
# Unlimited Data

telecom_DF['Online Security'].value_counts()


# In[49]:


# Monthly Charge
# Total Charges
# Total Refunds
# Total Extra Data Charges
# Total Long Distance Charges
# Total Revenue

col1 = telecom_DF['Churn Category'].value_counts()
col2 = telecom_DF['Churn Reason'].value_counts()
col1, col2

col1=telecom_DF['Churn Category']
col2=telecom_DF['Churn Reason']
result2=pd.crosstab(col1,col2)
result2


# In[54]:


plt.figure(figsize=(10,10))
corr=telecom_DF.corr(numeric_only=True)
sns.heatmap(corr,annot=True)


# In[61]:


Online_Security = telecom_DF['Online Security'].value_counts()
Online_Backup = telecom_DF['Online Backup'].value_counts()
Device_protection = telecom_DF['Device Protection Plan'].value_counts()
Premium_tech = telecom_DF['Premium Tech Support'].value_counts()
Str_TV = telecom_DF['Streaming TV'].value_counts()
Str_Movie = telecom_DF['Streaming Movies'].value_counts()
Str_Music = telecom_DF['Streaming Music'].value_counts()
Unlimited_data = telecom_DF['Unlimited Data'].value_counts()
d1 = pd. (Device_protection)
np.where(pd.isnull(d1))




# In[ ]:





# In[ ]:




