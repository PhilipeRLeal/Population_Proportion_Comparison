
# coding: utf-8

# In[ ]:



# coding: utf-8

# In[2]:


# Teste Chi^2 conforme Portal Action
    # http://www.portalaction.com.br/en/node/848
    
import numpy as np
import pandas as pd
from scipy.stats import chi2

# Teste Chi^2 conforme Portal Action
    # http://www.portalaction.com.br/en/node/848
    
import numpy as np
import pandas as pd
from scipy.stats import chi2


class Chi2_Test_in_DF(object):
    
    def __init__(self, df, alfa=0.05):
        """
        This class evaluates the probability of M classes having 
        the same proportion (ex: n° of occurence)
        
        Ho: assumes that all classes have the same proportion
        
        ha: assumes that at leaast one class(mi) has a different proportion than the rest  
        
        
        """
        
        self.DF = df
        self.Esperado = self.get_esperado
        self.Chi2 = (self.DF - self.Esperado)**2/self.Esperado
        
        Q2_sum = self.Chi2.sum().sum()
        
        print(Q2_sum)
        
        df = (self.DF.shape[0] -1) * (self.DF.shape[1] -1)

        P_value = (1 - chi2.cdf(Q2_sum, df))

        if P_value> alfa:
            self.Ho = True
            print("There is evidence that all classes", "\n" ,"have the same proportion (n° of occurence)")
        else:
            self.Ho=False
        
        self.Results = pd.Series({'Chi2':Q2_sum, 'P_value':P_value, 'H0 acceptance':self.Ho})
        
    
    @property
    def get_esperado(self):
        Esperado = self.DF.sum(axis=1) / self.DF.shape[1]
        
        Esperado = pd.DataFrame(np.repeat(Esperado.values, repeats=self.DF.shape[1]).reshape(self.DF.shape[0], self.DF.shape[1]))

        Esperado.columns = self.DF.columns


        Esperado.index = self.DF.index

        self.Esperado = Esperado
        
        return self.Esperado


