#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


## Data Frame

file_location="D:\\data_Science\\Data_For_Working\\Visadataset.csv"
visa_df=pd.read_csv(file_location)

visa_df
p_wage=visa_df['prevailing_wage']
print(p_wage)
print(p_wage.count())
print(p_wage.mean())
print(p_wage.median())
print(p_wage.max())
print(p_wage.min())

wage_count=p_wage.count()
wage_mean=p_wage.mean()
wage_median=p_wage.median()
wage_max=p_wage.max()
wage_min=p_wage.min()

list1= [wage_count,wage_mean,wage_median,wage_max,wage_min]
index_list=['count','max','min','mean','median']
list1
pd.DataFrame(list1,
            columns=['prevailing_wage'],
            index=index_list)


# In[17]:


pd.DataFrame(zip([1,2],[3,4],[4,5]))


# In[4]:


#number column seperately

num_cols1=visa_df.select_dtypes(exclude='object').columns
dict3={}
for i in num_cols1:
    count=visa_df[i].count()
    mean=round(visa_df[i].mean(),2)
    median=round(visa_df[i].median(),2)
    maxx=visa_df[i].max()
    minn=visa_df[i].min()
    list2=[count,mean,median,maxx,minn]
    dict3[i]=list2
index_list2=['count','mean','median','maxx','minn']
print(dict3)
number_df=pd.DataFrame(dict3,index=index_list2)
#number_df.to_csv("Number_df.csv")



# In[ ]:


np.where()

