
.. code:: python

    import numpy as np
    import scipy as sp
    from matplotlib import pyplot as plt
    
    np.set_printoptions(precision=5, suppress = True)
Problem 1.a.
            

.. code:: python

    maze = [[.5, .5, 0], [.25, .5, .25], [0, .5, .5]]
    maze = np.array(maze)
    
    print "Transition probability matrix:"
    print maze
    for power in [2, 5, 10, 25]:
        print "Transition probabilities after %d steps" %power
        print np.linalg.matrix_power(maze, power)

.. parsed-literal::

    Transition probability matrix:
    [[ 0.5   0.5   0.  ]
     [ 0.25  0.5   0.25]
     [ 0.    0.5   0.5 ]]
    Transition probabilities after 2 steps
    [[ 0.375  0.5    0.125]
     [ 0.25   0.5    0.25 ]
     [ 0.125  0.5    0.375]]
    Transition probabilities after 5 steps
    [[ 0.26562  0.5      0.23438]
     [ 0.25     0.5      0.25   ]
     [ 0.23438  0.5      0.26562]]
    Transition probabilities after 10 steps
    [[ 0.25049  0.5      0.24951]
     [ 0.25     0.5      0.25   ]
     [ 0.24951  0.5      0.25049]]
    Transition probabilities after 25 steps
    [[ 0.25  0.5   0.25]
     [ 0.25  0.5   0.25]
     [ 0.25  0.5   0.25]]


Problem 1.b.
            

.. code:: python

    maze = [[1, 0, 0], [.25, .5, .25], [0, 0, 1]]
    maze = np.array(maze)
    
    print "Transition probability matrix with absorbing states:"
    print maze
    for power in [2, 5, 10, 25]:
        print "Transition probabilities after %d steps" %power
        print np.linalg.matrix_power(maze, power)

.. parsed-literal::

    Transition probability matrix with absorbing states:
    [[ 1.    0.    0.  ]
     [ 0.25  0.5   0.25]
     [ 0.    0.    1.  ]]
    Transition probabilities after 2 steps
    [[ 1.     0.     0.   ]
     [ 0.375  0.25   0.375]
     [ 0.     0.     1.   ]]
    Transition probabilities after 5 steps
    [[ 1.       0.       0.     ]
     [ 0.48438  0.03125  0.48438]
     [ 0.       0.       1.     ]]
    Transition probabilities after 10 steps
    [[ 1.       0.       0.     ]
     [ 0.49951  0.00098  0.49951]
     [ 0.       0.       1.     ]]
    Transition probabilities after 25 steps
    [[ 1.   0.   0. ]
     [ 0.5  0.   0.5]
     [ 0.   0.   1. ]]


Problem 1.c.
            

.. code:: python

    maze = [[  1,   0,   0,   0,   0],
            [.25,  .5, .25,   0,   0],
            [  0, .25,  .5, .25,   0],
            [  0,   0, .25,  .5, .25],
            [  0,   0,   0,  .5,  .5]]
    maze = np.array(maze)
    
    print "Transition probability matrix:"
    print maze
    
    for power in [84, 125]:
        print "Transition probabilities after %d iterations:" %power
        print np.linalg.matrix_power(maze, power)


.. parsed-literal::

    Transition probability matrix:
    [[ 1.    0.    0.    0.    0.  ]
     [ 0.25  0.5   0.25  0.    0.  ]
     [ 0.    0.25  0.5   0.25  0.  ]
     [ 0.    0.    0.25  0.5   0.25]
     [ 0.    0.    0.    0.5   0.5 ]]
    Transition probabilities after 84 iterations:
    [[ 1.       0.       0.       0.       0.     ]
     [ 0.98153  0.00281  0.0052   0.00679  0.00367]
     [ 0.96587  0.0052   0.0096   0.01255  0.00679]
     [ 0.9554   0.00679  0.01255  0.01639  0.00887]
     [ 0.95173  0.00735  0.01358  0.01774  0.0096 ]]
    Transition probabilities after 125 iterations:
    [[ 1.       0.       0.       0.       0.     ]
     [ 0.99624  0.00057  0.00106  0.00138  0.00075]
     [ 0.99305  0.00106  0.00196  0.00256  0.00138]
     [ 0.99091  0.00138  0.00256  0.00334  0.00181]
     [ 0.99017  0.0015   0.00277  0.00361  0.00196]]


