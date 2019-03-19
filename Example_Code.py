
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import os, sys


# In[10]:


path = os.path.dirname(os.path.realpath('__file__'))

sys.path.insert(0, path)

from Chi2_Test import Chi2_Test_in_DF


# In[12]:


DF = pd.read_excel(r'Independencia.xls')


DF


# In[13]:



Results_of_test = Chi2_Test_in_DF(DF).Results

Results_of_test

