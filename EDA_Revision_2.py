#!/usr/bin/env python
# coding: utf-8

# In[13]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_location="D:\\data_Science\\Data_For_Working\\visadataset.csv"
visa_df=pd.read_csv(file_location)
visa_df.head()

visa_df.dtypes

p_wage=visa_df['prevailing_wage']
p_wage.median()


# In[19]:


p_wage=visa_df['prevailing_wage']
wage_count=p_wage.count()
wage_mean=round(p_wage.mean(),2)
wage_median=round(p_wage.median(),2)
wage_max=round(p_wage.max(),2)
wage_min=round(p_wage.min(),2)
list1=[wage_count,wage_mean,wage_median,wage_max,wage_min]
index_list=['count','mean','median','max','min']
pd.DataFrame(list1,
            columns=['prevailing_wage'],
            index=index_list)


# In[28]:


# Numerical columns seperaetly
num_col=visa_df.select_dtypes(exclude='object').columns
#num_col
dict1={}
for i in num_col:
    count=visa_df[i].count()
    mean=visa_df[i].mean()
    median=visa_df[i].median()
    maxx=visa_df[i].max()
    minn=visa_df[i].min()    
    list1=[count, mean, median, maxx, minn]
    dict1[i]=list1

index_list=['count','max','min','mean','median']
numer_df=pd.DataFrame(dict1,index=index_list)
numer_df


# In[30]:


visa_df.describe()


# In[31]:


p_wage=visa_df['prevailing_wage']
wage_count=p_wage.count()
wage_mean=round(p_wage.mean(),2)
wage_median=round(p_wage.median(),2)
wage_max=round(p_wage.max(),2)
wage_min=round(p_wage.min(),2)
wage_std=round(p_wage.std(),2)
list1=[wage_count,wage_max,wage_min,
 wage_mean,wage_median,wage_std]
index_list=['count','max','min','mean','median','std']
pd.DataFrame(list1,
 columns=['prevailing_wage'],
 index=index_list)


# In[33]:


p_wage=visa_df['prevailing_wage']
p_50=np.percentile(p_wage,50)
con=p_wage<p_50
con
#visa_df[con]


# In[34]:


p_wage=visa_df['prevailing_wage']
p_25=np.percentile(p_wage,25)
p_50=np.percentile(p_wage,50)
# between 25p to 50p
con1=p_wage>p_25
con2=p_wage<p_50
visa_df[con1&con2]


# In[36]:


p_wage =visa_df['prevailing_wage']
p_25 = np.percentile(p_wage,25)
p_75 = np.percentile(p_wage,75)
con_1 = p_wage<p_25
con_2 = p_wage>p_75
visa_df[con_1 | con_2]


# In[41]:


p_wage=visa_df['prevailing_wage']
freq,interval,n=plt.hist(p_wage,bins=40)
freq,interval


# In[43]:


plt.hist(p_wage,bins=40)


# In[45]:


pd.DataFrame(zip(freq,interval),columns=["Frequency","Intervel"])


# In[47]:


plt.hist(p_wage,bins=40)

