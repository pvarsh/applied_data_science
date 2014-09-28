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

def scPlotsFig(dfIn, ncols = 3, fileOut = None, outFormat = 'png', linreg = False):
  # makes scatter plots of all columns against last columns on one figure
  # parameters:
  #   dfIn:      data frame containing m columns,
  #              the first m-1 columns will be plotted against mth column
  #   ncols:     number of columns in figure
  #   fileOut:   figure output file name with path. default will print to screen
  #   outFormat: file format to print to. default will print to 'png'
  #   linreg:    include linear regression lines (True/False)
  # TODO: parse fileOut to extract format
  
  # get column names for all but last column
  cols1c = list(dfIn.columns.values)[0:-1]
  
  # summary stats for dfIn
  dfSummary = dfIn.describe()

  # set y limits
  ymin, ymax = dfSummary['lw'][[3,-1]]
  ywidth = ymax - ymin
  ymin, ymax = ymin - 0.1 * ywidth, ymax + 0.1 * ywidth
 
  # create figure 
  fig = plt.figure()
  
  # calculate number of rows and plots per row
  nplots = len(cols1c)
  nrows = int(ceil(float(nplots/ncols)))

  # create plots in fig
  for i, col in enumerate(cols1c):
    subPlotPosition = int(str(nrows) + str(ncols) + str(i+1))
    #print subPlotPosition 
    fig.add_subplot(subPlotPosition)
    plt.plot(dfIn[col], dfIn['lw'], 'co')

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
    regOut = stats.linregress(dfIn[col], dfIn['lw'])
    plt.plot([xmin, xmax], [regOut[0]* v + regOut[1] for v in [xmin, xmax]], 'r-')

  # adjust space between plots
  plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=.3, hspace=.5)
  
  # print to screen or to file
  if fileOut != None:
    plt.savefig(fileOut, format = outFormat) 
  else:
    plt.show()

scPlotsFig(df[cols1b], ncols = 3, fileOut = figurespath + "fig1c.pdf", outFormat = 'pdf')


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
