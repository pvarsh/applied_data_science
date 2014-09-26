##############################
# Applied Data Science
# HW 3
# Peter Varshavsky
##############################
import numpy as np
import pandas as pd

path = "/Users/petervarshavsky/Documents/Git_NYU/applied_data_science/assignment_3/"
grilFile = "griliches.dta"

fileGril = path + grilFile 

df = pd.read_stata(fileGril)
print df.head()

print df.describe()

#x = {'a': [1,2,3],
#     'b': ['foo']*3,
#     'd': np.array([3,2,1], dtype = 'int32')}
#print x
#
#df2 = pd.DataFrame(x)
#print df2.head()
#print df2.dtypes
#print "indexaaaaa: "
#print df2.index
#print "columnsasdfasdf: "
#print df2.columns
#print "valuesdfasdjf: "
#print df2.values


