
# coding: utf-8

## Applied Data Science: Lab 1

#### Setting up

# In[191]:

### imports
import math
import numpy as np
import scipy as sp
import pandas as pd
from matplotlib import pyplot as plt
import statsmodels.api as sm
import patsy
import re

get_ipython().magic(u'matplotlib inline')

### functions

### read file
filepath = "/Users/petervarshavsky/Documents/Git_NYU/applied_data_science/lab-1/data/"
traff_file = filepath + "trafficking_data.csv"
traff = pd.read_csv(traff_file)

### clean column names
colNames = traff.columns.values.tolist()
colNames = [col.lower() for col in colNames]
colNames = [re.sub(' ', '_', col) for col in colNames]
colNames[7] = "percent_fem_educ"
traff.columns = colNames

### clean country names
cNames = {country: country.title() for country in traff.country}
cNames['United Arab Emirate'] = 'United Arab Emirates'
cNames['Viet Nam'] = 'Vietnam'
traff.country = [cNames[c] for c in traff.country]

### total victims
traff['total_victims'] = traff.child_victims + traff.adult_victims
columns = traff.columns.values.tolist()
columns_reorder = ['country', 'year', 
                   'persons_prosecuted', 'adult_victims', 
                   'child_victims', 'total_victims', 'gdp',
                   'policy_index', 'percent_fem_educ',
                   'life_expectancy']
traff = traff[columns_reorder]

### checking columns for missing data

print "Missing values in columns:\n",  traff.isnull().sum()[traff.isnull().sum() > 0]
print traff.shape

### removing missing values
traff = traff[traff.child_victims.notnull()]
print traff.shape


#### Problem 1: Checking predictive power

####### Modeling adult_victims

# In[192]:

### All predictors including country names (obviously a bad model)
# all_columns = traff.columns.values.tolist()
# y, X = patsy.dmatrices('adult_victims ~ country + year + policy_index + percent_fem_educ + life_expectancy',
#                        data = traff,
#                        return_type='dataframe')

# everything_bagel = sm.OLS(y, X)
# results_everything  = everything_bagel.fit()
# print results_everything.summary()

### All predictors excluding country names
y, X = patsy.dmatrices('adult_victims ~ gdp + year + policy_index + percent_fem_educ + life_expectancy + persons_prosecuted',
                        data = traff,
                        return_type='dataframe')
main_effects_fit = sm.OLS(y, X).fit()
print main_effects_fit.summary()

### Comparing all bivariates
#print traff.columns.values
cols = ['year', 'gdp', 'policy_index', 'percent_fem_educ', 'life_expectancy', 'persons_prosecuted']
bivariate_dmatrices = [patsy.dmatrices('adult_victims ~ ' + col,
                                       data = traff,
                                       return_type = 'dataframe') for col in cols]
bivariate_fits = [sm.OLS(dmatrix[0], dmatrix[1]).fit() for dmatrix in bivariate_dmatrices]

for fit in bivariate_fits:
    print '####################'
    print '####################'
    print fit.summary()

    


##### Modeling child_victims

# In[193]:

### All predictors excluding country names
y, X = patsy.dmatrices('child_victims ~ gdp + year + policy_index + percent_fem_educ + life_expectancy + persons_prosecuted',
                        data = traff,
                        return_type='dataframe')
main_effects_fit = sm.OLS(y, X).fit()
print main_effects_fit.summary()

### Comparing all bivariates
#print traff.columns.values
cols = ['year', 'gdp', 'policy_index', 'percent_fem_educ', 'life_expectancy', 'persons_prosecuted']
bivariate_dmatrices = [patsy.dmatrices('child_victims ~ ' + col,
                                       data = traff,
                                       return_type = 'dataframe') for col in cols]
bivariate_fits = [sm.OLS(dmatrix[0], dmatrix[1]).fit() for dmatrix in bivariate_dmatrices]

for fit in bivariate_fits:
    print '####################'
    print '####################'
    print fit.summary()

    


####### Modeling persons_prosecuted

# In[194]:

### All predictors excluding country names
y, X = patsy.dmatrices('persons_prosecuted ~ gdp + year + policy_index + percent_fem_educ + life_expectancy',
                        data = traff,
                        return_type='dataframe')
main_effects_fit = sm.OLS(y, X).fit()
print main_effects_fit.summary()

### Comparing all bivariates
#print traff.columns.values
cols = ['year', 'gdp', 'policy_index', 'percent_fem_educ', 'life_expectancy']
bivariate_dmatrices = [patsy.dmatrices('persons_prosecuted ~ ' + col,
                                       data = traff,
                                       return_type = 'dataframe') for col in cols]
bivariate_fits = [sm.OLS(dmatrix[0], dmatrix[1]).fit() for dmatrix in bivariate_dmatrices]

for fit in bivariate_fits:
    print '####################'
    print '####################'
    print fit.summary()


#### Problem 2. Removing outliers

# In[231]:

print traff.columns.values.tolist()
cols = ['persons_prosecuted', 'adult_victims', 'child_victims', 'total_victims', 'gdp', 'policy_index', 'percent_fem_educ', 'life_expectancy']

print traff[['country', 'year', 'persons_prosecuted']][traff.persons_prosecuted > 15000]
print traff[['country', 'year', 'child_victims']][traff.child_victims > 300]
print traff[['country', 'year', 'gdp']][traff.gdp > 0.3*1e13]
print traff[['country', 'year', 'policy_index']][traff.policy_index < 2]

### plotting histograms
for col in cols:
    plt.hist(traff[col], bins=15, color='orange')
    plt.xlabel(col)
    plt.show()
    


# # for col in cols:
# #     plt.hist(np.log(traff[col]), bins=15, color='cyan')
# #     plt.xlabel('log ' + col)
# #     plt.show()

# ### persons_prosecuted outliers
# print traff.country[traff.persons_prosecuted > 5000]
# traffOutRem = traff[traff.persons_prosecuted < 5000]
# print traff.shape
# print traffOutRem.shape

# ### All predictors excluding country names
# y, X = patsy.dmatrices('adult_victims ~ gdp + year + policy_index + percent_fem_educ + life_expectancy',
#                         data = traffOutRem,
#                         return_type='dataframe')
# main_effects_fit = sm.OLS(y, X).fit()
# print main_effects_fit.summary()

# y, X = patsy.dmatrices('child_victims ~ gdp + year + policy_index + percent_fem_educ + life_expectancy',
#                         data = traffOutRem,
#                         return_type='dataframe')
# main_effects_fit = sm.OLS(y, X).fit()
# print main_effects_fit.summary()

# y, X = patsy.dmatrices('total_victims ~ gdp + year + policy_index + percent_fem_educ + life_expectancy',
#                         data = traffOutRem,
#                         return_type='dataframe')
# main_effects_fit = sm.OLS(y, X).fit()
# print main_effects_fit.summary()


####### Looking at child_victims main effects model. 

# In[232]:

y, X = patsy.dmatrices('child_victims ~ percent_fem_educ + life_expectancy + persons_prosecuted',
                        data = traffOutRem,
                        return_type='dataframe')
main_effects_fit = sm.OLS(y, X).fit()
print main_effects_fit.summary()


#### Problem 3. Log transform

####### Log transofrm and -inf substitution

# In[177]:

### log transform
# traffNumeric = traffOutRem._get_numeric_data()
# traffNumeric = np.log(traffNumeric)
# ### change -inf to 1
# traffNumeric[traffNumeric == -np.inf] = 1
# ### change names
# names = traffNumeric.columns.values.tolist()
# for i in range(len(names)):
#     names[i] = 'log_' + names[i]
# traffNumeric.columns = names

# print traffNumeric.head

# traffOutRem = pd.concat([traffOutRem, traffNumeric], axis = 0)


# In[185]:

y, X = patsy.dmatrices('log_child_victims ~ log_gdp + log_life_expectancy + log_percent_fem_educ + log_persons_prosecuted + log_policy_index', data = traffOutRem, return_type = 'dataframe')
log_fit = sm.OLS(y, X).fit()
print log_fit.summary()


# In[241]:

### Reading internet penetration by country
print filepath
penetration_file = "internet-penetration-by-country.csv"
penetration = pd.read_csv(filepath + "internet-penetration-by-country.csv")



# In[ ]:



