##############################
# Applied Data Science
# HW 3
# Peter Varshavsky
##############################
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from scipy import stats
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

cols1c = ['rns', 'mrt', 'smsa', 'kww', 'expr', 'lw']
       
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

def scPlotsFig(dfIn, ncols = 3, fileOut = None, outFormat = 'png', linReg = False, suptitle = None):
  # makes scatter plots of all columns against last columns on one figure
  # parameters:
  #   dfIn:      data frame containing m columns,
  #              the first m-1 columns will be plotted against mth column
  #   ncols:     number of columns in figure
  #   fileOut:   figure output file name with path. default will print to screen
  #   outFormat: file format to print to. default will print to 'png'
  #   linReg:    include linear regression lines (True/False)
  # TODO: parse fileOut to extract format
  # TODO: change 'lw' in subsetting to last column that does not depend on name
  
  # get column names for all but last column
  indepCols = list(dfIn.columns.values)[0:-1]
  
  # summary stats for dfIn
  dfSummary = dfIn.describe()

  # set y limits
  ymin, ymax = dfSummary['lw'][[3,-1]]
  ywidth = ymax - ymin
  ymin, ymax = ymin - 0.1 * ywidth, ymax + 0.1 * ywidth
 
  # create figure 
  fig = plt.figure()
  
  # calculate number of rows and plots per row
  print "# columns:", ncols
  nplots = len(indepCols)
  print "# plots: ", nplots
  nrows = int(ceil(float(nplots)/ncols))
  print "# rows: ", nrows
  
  # create plots in fig
  for i, col in enumerate(indepCols):
    subPlotPosition = int(str(nrows) + str(ncols) + str(i+1))
    fig.add_subplot(subPlotPosition)
    plt.plot(dfIn[col], dfIn['lw'], linestyle = 'None', marker = 'o', fillstyle = 'none', color = 'c')

    # add x-axis annotation
    plt.xlabel(col)
   
    # y-axis label only for first plot in each row
    if i % ncols == 0:
      plt.ylabel('log wage')
    xmin, xmax = dfSummary[col][[3, -1]]
    xwidth = xmax - xmin
    xmin, xmax = xmin - 0.1 * xwidth, xmax + 0.1 * xwidth
    plt.axis([xmin, xmax, ymin, ymax])
  
    # add regression line
    if linReg == True:
      regOut = stats.linregress(dfIn[col], dfIn['lw'])
      plt.plot([xmin, xmax], [regOut[0]* v + regOut[1] for v in [xmin, xmax]], linestyle='-', linewidth = 2, color = '#EE9A00') 

  # adjust space between plots
  plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=.3, hspace=.5)
  
  # add figure suptitle 
  if suptitle != None:
    plt.suptitle(suptitle)  

  # print to screen or to file
  if fileOut != None:
    plt.savefig(fileOut, format = outFormat) 
  else:
    plt.show()


## Problem 1c, 1d.
# print to file
#scPlotsFig(df[cols1c], ncols = 2, fileOut = figurespath + "fig1c.pdf", outFormat = 'pdf', linReg = True, suptitle = "Problem 1b, 1c")
# print to screen
#scPlotsFig(df[cols1c], ncols = 2, linReg = True, suptitle = "Problem 1b, 1c")

## Problem 1d p values
for col in cols1c[:-1]:
  slope, intercept, rValue, pValue, stdErr = stats.linregress(df[col], df[cols1c[-1]])
  print col.upper()
  print "slope, stdErr, P Value: %f, %f, %f" %(slope, stdErr, pValue)
  print "(%f, %f)" %(slope - 2*stdErr, slope + 2*stdErr) 

## Problem 1e. 95%CI
degFree = len(df['lw'])
slope, intercept, rvalue, pvalue, stdErr = stats.linregress(df.s, df.lw)
t_quant95 = stats.t.ppf([0.025, 0.975], degFree)
print "Estimated model: lw = %4.3f + %4.3f S" %(intercept, slope)
print "95%% CI for b_1: (%f, %f)" %(slope + stdErr * t_quant95[0], slope + stdErr * t_quant95[1])





#scPlotsFig(df[cols1c], ncols = 3, linReg = True)

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
