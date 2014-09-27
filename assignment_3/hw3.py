##############################
# Applied Data Science
# HW 3
# Peter Varshavsky
##############################
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from math import ceil

import csv




# set up paths to data, tables, figures directories
hwpath = "/Users/petervarshavsky/Documents/Git_NYU/applied_data_science/assignment_3/"
datapath = hwpath + "data/"
tablespath = hwpath + "tables/"
figurespath = hwpath + "figures/"

## data filename for problem 1
grilFile = datapath + "griliches.dta"

## read data
df = pd.read_stata(grilFile)

## columns for problem 1b
cols1b = ['rns', 'mrt', 'smsa', 'med', 'iq',
       'kww', 'age', 's', 'expr',
       'lw']
       
## output description to screen
#print df[cols1b].describe()

## output description to csv
#df[cols1b].describe().to_csv(tablespath + "table1b.csv")

## 1.c. plots

def scPlots(dfIn):
  # makes scatter plots of all columns against last columns
  # get column names for all but last column
  cols1c = list(dfIn.columns.values)[0:-1]
  
  # summary stats for dfIn
  dfSummary = dfIn.describe()

  # set y limits
  ymin, ymax = dfSummary['lw'][[3,-1]]
  ywidth = ymax - ymin
  ymin, ymax = ymin - 0.05 * ywidth, ymax + 0.05 * ywidth
  
  #cols1c = ['rns', 'mrt', 'smsa', 'kww', 'expr']
  
  #df1c = df[cols1c].describe()
  #ymin, ymax = df[cols1b].describe()['lw'][[3,-1]]
  #ywidth = ymax - ymin
  #ymin, ymax = ymin - 0.05 * ywidth, ymax + 0.05 * ywidth
  
  fig = plt.figure()
  
  nplots = len(cols1c)

  for col in cols1c:
    plt.plot(dfIn[col], dfIn['lw'], 'co')
    plt.xlabel(col)
    plt.ylabel('log wage')
    xmin, xmax = dfSummary[col][[3, -1]]
    xwidth = xmax - xmin
    xmin, xmax = xmin - 0.05 * xwidth, xmax + 0.05 * xwidth
      
    plt.axis([xmin, xmax, ymin, ymax])
    plt.show()

def scPlotsFig(dfIn, ncols = 3):
  # makes scatter plots of all columns against last columns on one figure
  
  # get column names for all but last column
  cols1c = list(dfIn.columns.values)[0:-1]
  
  # summary stats for dfIn
  dfSummary = dfIn.describe()

  # set y limits
  ymin, ymax = dfSummary['lw'][[3,-1]]
  ywidth = ymax - ymin
  ymin, ymax = ymin - 0.05 * ywidth, ymax + 0.05 * ywidth
  
  fig = plt.figure()
  
  nplots = len(cols1c)
  nrows = int(ceil(float(nplots/ncols)))

  for i, col in enumerate(cols1c):
    subPlotPosition = int(str(nrows) + str(ncols) + str(i+1))
    #print subPlotPosition 
    ax = fig.add_subplot(subPlotPosition)
    ax.plot(dfIn[col], dfIn['lw'], 'co')
    ax.plt.xlabel(col)
    #ax.ylabel('log wage')
    #xmin, xmax = dfSummary[col][[3, -1]]
    #xwidth = xmax - xmin
    #xmin, xmax = xmin - 0.05 * xwidth, xmax + 0.05 * xwidth
      
    #ax.plt.axis([xmin, xmax, ymin, ymax])
  plt.show()

scPlotsFig(df[cols1b])

#scPlots(df[cols1b])
#fout = "table1b.csv"
#with open(fout, 'r') as f:
#  writer = csv.writer(f)
#  writer.writerows(df[cols1b].describe()
    
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
