#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_location="D:\\data_Science\\Data_For_Working\\visadataset.csv"
visa_df=pd.read_csv(file_location)
visa_df.head()


#For outliars
plt.boxplot(visa_df['prevailing_wage'])


# In[13]:


# Step-1
# Calculate Q1 Q2 and Q3
Q1=np.quantile(visa_df['prevailing_wage'],0.25)
Q2=np.quantile(visa_df['prevailing_wage'],0.50)
Q3=np.quantile(visa_df['prevailing_wage'],0.75)
Q1,Q2,Q3

#step-2
IQR=Q3-Q1
IQR

#step-3
UB=Q3+1.5*IQR
LB=Q1-1.5*IQR
UB,LB

#Step-4
#>UB <LB are the outliers
con1=visa_df['prevailing_wage']>UB
con2=visa_df['prevailing_wage']<LB

#Step-5
# if you apply | with outlier
outliers_df=visa_df[con1|con2]
outliers_df


# In[17]:


def outliers(col):
 Q1=np.quantile(visa_df[col],0.25)
 Q2=np.quantile(visa_df[col],0.50)
 Q3=np.quantile(visa_df[col],0.75)
 IQR=Q3-Q1
 UB=Q3+1.5*IQR
 LB=Q1-1.5*IQR
 con1=visa_df[col]>UB
 con2=visa_df[col]<LB
 outliers_df=visa_df[con1|con2]
 print(f'{col} has {len(outliers_df)} outliers')
 print('{} has {} outliers'.format(col,len(outliers_df)))
 
 
num_col=visa_df.select_dtypes(exclude='object').columns
for col in num_col: 
    outliers(col)


# In[22]:


Q1=np.quantile(visa_df['prevailing_wage'],0.25)
Q2=np.quantile(visa_df['prevailing_wage'],0.50)
Q3=np.quantile(visa_df['prevailing_wage'],0.75)
IQR=Q3-Q1
UB=Q3+1.5*IQR
LB=Q1-1.5*IQR
############ Outliers df #################
con1=visa_df['prevailing_wage']>UB
con2=visa_df['prevailing_wage']<LB
outliers_df=visa_df[con1|con2]
########## Non outliers df ###############
con11=visa_df['prevailing_wage']<UB
con22=visa_df['prevailing_wage']>LB
non_outliers_df=visa_df[con11&con22]

len(non_outliers_df),len(outliers_df)


# In[26]:


plt.figure(figsize=(10,8))
plt.subplot(2,2,1)
plt.boxplot(visa_df['prevailing_wage'],vert=False) # 25480
plt.subplot(2,2,2)
plt.boxplot(non_outliers_df['prevailing_wage'],vert=False) # 25053
plt.subplot(2,2,3)
plt.boxplot(outliers_df['prevailing_wage'],vert=False) # 25053
plt.subplot(2,2,4)
plt.hist(outliers_df['prevailing_wage'],bins=40)
plt.show()


# In[28]:


visa_df['continent'].value_counts()


# In[33]:


con1=visa_df['continent']=='Asia'
con2=visa_df['case_status']=='Certified'
con=con1&con2
len(visa_df[con])
con1


# In[48]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_location="D:\\data_Science\\Data_For_Working\\visadataset.csv"
visa_df=pd.read_csv(file_location)
visa_df.head()

labels=visa_df['continent'].value_counts().keys()
labels
certified=[]
denied=[]
for i in labels:
    con1=visa_df['continent']==i
    con2=visa_df['case_status']=='Certified'
    con3=visa_df['case_status']=='Denied'
    cert_con=con1&con2
    denied_con=con1&con3
    certified.append(len(visa_df[cert_con]))
    denied.append(len(visa_df[denied_con]))

d1=pd.DataFrame(zip(labels,Certified,denied),
                columns=['Continent','Certified','Denied'])
d1.set_index('Continent')


# In[ ]:





# In[ ]:





# In[ ]:




