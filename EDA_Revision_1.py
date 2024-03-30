#!/usr/bin/env python
# coding: utf-8

# In[34]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

file_location = "D:\\data_Science\\Data_For_Working\\visadataset.csv"

visa_df=pd.read_csv(file_location)

visa_df.head()
visa_df.tail()
visa_df.shape
shape_of_visa_df=(visa_df.shape)
shape_of_visa_df[0]
len(visa_df)
visa_df.columns
cols_to_list=(visa_df.columns)
type(cols_to_list)
type(cols_to_list)
list1=cols_to_list.to_list()
type(list1)
list1
visa_df.dtypes

visa_df.info(0)


# In[38]:


visa_df.dtypes
dtype=dict(visa_df.dtypes)
dtype

for i in dtype:
    if(dtype[i]=="object"):
        print(dtype[i])
        
cat_col=[i for i in dtype if(dtype[i]=="object")]
Num_col=[i for i in dtype if(dtype[i]!="object")]

cat_col, Num_col
    


# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

file_location = "D:\\data_Science\\Data_For_Working\\visadataset.csv"
visa_df=pd.read_csv(file_location)
list(visa_df['continent'].values)


# In[4]:


l1=[1,2,3,4]
l2=[11,22,33,44]
l3=l1+l2
l3


a1=np.array(l1)
a2=np.array(l2)
a1+a2


# In[17]:


cols=['continent','education_of_employee']
visa_df[cols]


# In[23]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

file_location = "D:\\data_Science\\Data_For_Working\\visadataset.csv"
visa_df=pd.read_csv(file_location)
len(visa_df)
visa_df['continent'].value_counts()


# In[51]:


continanat_values=dict(visa_df['continent'].value_counts())
continanat_values
keys=list(continanat_values.keys())
values=list(continanat_values.values())
continent_df=pd.DataFrame(zip(keys,values),
                         columns=['Continent','Count'])
continent_df


# In[48]:


continent_values=dict(visa_df['continent'].value_counts())
pd.DataFrame(continent_values,index=['Count'])


# In[55]:


plt.figure(figsize=(10,5))
plt.bar('Continent','Count',data=continent_df)
plt.xlabel("Continents")
plt.ylabel("Count")
plt.title("Bar chart")
#plt.savefig("Continent_bar_chart.jpg")
plt.show()


# In[58]:


values=visa_df['continent'].value_counts(normalize=True)
values


# In[65]:


# x= values
# labels= keys
keys=visa_df['continent'].value_counts().keys()
values=visa_df['continent'].value_counts().to_list()
plt.pie(x=values,
 labels=keys,
 autopct="%0.2f%%",
 #explode=[0.1,0.1,0.1,0.1,0.1,0.1],
 #shadow=True,
 startangle=180,
 radius=2)
plt.show()

