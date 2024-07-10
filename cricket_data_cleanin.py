#!/usr/bin/env python
# coding: utf-8

# In[101]:


import pandas as pd


# In[102]:


df = pd.read_csv(r'C:\Users\Admin\Desktop\csv files\cricket_data.csv')
df


# In[103]:


df.shape


# In[104]:


df.columns


# In[105]:


df = df.rename(columns = {'Mat' : 'Match_played', 
                          'Inns' : 'Inning_batted',
                          'NO' : 'Not_outs',
                          'HS' : 'Highest_inns_score',
                          'Ave' : 'Batted_average',
                          'BF' : 'Balls_faced',
                          'SR' : 'Strike_rate',
                           })
df.head()


# In[106]:


df.isna().sum()


# In[107]:


df[df.duplicated()]


# In[108]:


df = df.loc[~df.duplicated()].reset_index(drop = True ).copy()


# In[109]:


df[df.duplicated()]


# In[110]:


df.isna().any()


# In[111]:


df[df['Balls_faced'].isna() == 1]


# In[112]:


df['Balls_faced'] = df['Balls_faced'].fillna(0)


# In[113]:


df[df['Balls_faced'].isna() == 1]


# In[114]:


df.head()


# In[115]:


df['Span']


# In[116]:


df['Span'].str.split(pat = '-')


# In[117]:


df['start_year'] = df['Span'].str.split(pat = '-').str[0]


# In[118]:


df['end_year'] = df['Span'].str.split(pat = '-').str[1]


# In[119]:


df


# In[120]:


df.drop('Span', axis = 1)


# In[121]:


df['Player'].str.split(pat = '(')


# In[122]:


df['Country'] = df['Player'].str.split(pat = '(').str[1]


# In[123]:


df['Country'] = df['Country'].str.split(pat = ')').str[0]


# In[124]:


df['Country'] = df['Country'].str[0]


# In[125]:


df['Country']


# In[126]:


df['Player'] = df['Player'].str.split(pat = '(').str[0]


# In[127]:


df.head()


# In[128]:


df = df.drop(['Span'], axis = 1)


# In[129]:


df['Highest_inns_score'].str.split(pat = '*').str[0]


# In[130]:


df['Highest_inns_score'] = df['Highest_inns_score'].str.split(pat = '*').str[0]


# In[131]:


df['Highest_inns_score'] = df['Highest_inns_score'].astype('int')


# In[132]:


df.dtypes


# In[133]:


df = df.astype({'start_year' : 'int', 'end_year' : 'int'})


# In[134]:


df.dtypes


# In[135]:


df.head(2)


# In[136]:


df['Career_length'] = df['end_year'] - df['start_year']
df


# In[144]:


df.groupby('Country')['Highest_inns_score'].max('Highest_inns_score').to_frame().sort_values('Highest_inns_score', ascending = True) 


# In[146]:


df['Career_length'].mean()


# In[147]:


filt = (df['Career_length'] > 10)


# In[148]:


df.loc[filt]['Strike_rate'].mean()


# In[149]:


filt = df['start_year'] > 1960


# In[150]:


df.loc[filt]['Player'].count()


# In[153]:


df.groupby(['Country'])['100'].mean().to_frame().sort_values('100', ascending = False)


# In[ ]:




