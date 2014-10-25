
.. code:: python

    ### imports
    import random
    import numpy as np
    import scipy as sp
    import pandas as pd
    import statsmodels.api as sm
    import patsy
    import csv
    
    from matplotlib import pyplot as plt
    import matplotlib.pylab as pylab
    
    ### settings
    %matplotlib inline
    pylab.rcParams['figure.figsize'] = 16, 5  # that's default image size for this interactive session
    np.set_printoptions(precision=5, suppress = True)
Problem 3.a.
            

.. code:: python

    x1 = np.random.normal(0, 1, 1000)
    x2 = np.random.normal(0, 2, 1000)
    x4 = np.random.normal(0, 4, 1000)
    
    plt.figure(1)
    plt.subplot(131)
    plt.ylim((-15, 15))
    plt.plot(x4, marker ='>', linestyle = 'None', color = '#ee9a00')
    plt.subplot(132)
    plt.ylim((-15, 15))
    plt.plot(x2, 'm<')
    plt.subplot(133)
    plt.ylim((-15, 15))
    plt.plot(x1, 'co')
    plt.savefig('problem3a.png', bbox_inches='tight')
    plt.show()



.. image:: assignment_4_3_files/assignment_4_3_2_0.png


Problem 3.b.
            

.. code:: python

    #X1 = np.random.normal(0,1,1000)
    #X2 = np.random.normal(0,1,1000)
    X_save = np.column_stack([X1, X2])
    X1_dm = sm.add_constant(X1) # dm for design matrix
    fit1 = sm.OLS(X2, X1_dm).fit()
    print sm.OLS(X2, X1_dm).fit().summary()
    plt.figure(2)
    plt.plot(X1, X2, marker = 'o', linestyle = 'None', color = "#ee9a00")
    plt.plot(X1, fit1.params[0] + fit1.params[1]*X1, 'c-')
    plt.savefig('problem3b.png', bbox_inches='tight')
    
    with open('strange_x.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['const', 'X1', 'X2'])
        writer.writerows(X_save)

.. parsed-literal::

                                OLS Regression Results                            
    ==============================================================================
    Dep. Variable:                      y   R-squared:                       0.008
    Model:                            OLS   Adj. R-squared:                  0.007
    Method:                 Least Squares   F-statistic:                     8.435
    Date:                Sat, 25 Oct 2014   Prob (F-statistic):            0.00376
    Time:                        18:33:53   Log-Likelihood:                -1460.1
    No. Observations:                1000   AIC:                             2924.
    Df Residuals:                     998   BIC:                             2934.
    Df Model:                           1                                         
    ==============================================================================
                     coef    std err          t      P>|t|      [95.0% Conf. Int.]
    ------------------------------------------------------------------------------
    const         -0.0014      0.033     -0.042      0.967        -0.066     0.063
    x1             0.0960      0.033      2.904      0.004         0.031     0.161
    ==============================================================================
    Omnibus:                        2.243   Durbin-Watson:                   2.051
    Prob(Omnibus):                  0.326   Jarque-Bera (JB):                2.315
    Skew:                           0.105   Prob(JB):                        0.314
    Kurtosis:                       2.894   Cond. No.                         1.02
    ==============================================================================



.. image:: assignment_4_3_files/assignment_4_3_4_1.png


.. code:: python

    fit1.params



.. parsed-literal::

    array([-0.00138,  0.09605])



Problem 3.c.
            

.. code:: python

    slopes = []
    for i in range(1000):
        z1 = np.random.normal(0,1,1000)
        z2 = np.random.normal(0,1,1000)
        z1_dm = sm.add_constant(z1) # dm for design matrix
        slope = sm.OLS(z2, z1_dm).fit().params[1]
        slopes.append(slope)
    
    plt.hist(slopes, color = "c")
    plt.savefig('problem3c.png', bbox_inches='tight')


.. image:: assignment_4_3_files/assignment_4_3_7_0.png


