
# Numbers from random.org
x = c(6,3,6,8,1,3,8,4,9,1)
y = c(0,5,3,0,0,6,5,9,3,8)

### Problem 1
problem1 = function(){
  cat("PROBLEM 1")
  # a.
  plot(x, y, main = "Problem 1.a")
  # b.
  cat("\nMean of x is", mean(x))
  cat("\nMean of y is", mean(y))
  # c.
  cat("\nVariance of x is", var(x))
  cat("\nVariance of y is", var(y))
  # d.
  cat("\nStandard deviation of x is", sd(x))
  cat("\nStandard deviation of y is", sd(y))
  # e.
  cat("\nCovariance of x and y is", cov(x,y))
  # f.
  cat("\nCorrelation of x and y is", cor(x,y))
  # g.
  slope = cov(x,y)/var(x)
  cat("\nThe slope of the regression line is cov(x,y) / var(x) =", slope)
  new.x = 13
  pred.y = mean(y) + slope * (new.x - mean(x))
  cat("\nFor x =", new.x, "the point estimate for y is y =", pred.y)
}
problem1()

### 2.
# a. Discrete. The number of rides taken by a resident in a month is a count variable that takes values on the set of natural numbers, which is discrete.
# b. Continuous. Bicyclist's speed can take any real value bounded from below by 0 and from above by the speed of light. No particular value of speed has probabily mass, only density.
# c. Continuous. Minute variations in lamps and current suggest a continuous variable. If the minute variations are not of interest, then the luminosity measurements can be converted to a discrete variable.
# d. Discrete. Assuming bankers cannot receive arbitrarily small fractions of a dollar, the salaries are discrete, however a continuous variable may be more convenient.
# e. Discrete. The number of hotels in Manhattan is a count variable.
# f. Continuous. Loudness is continuous.
# g. Discrete. Coffee can be 'good or bad' or 'very good, good, average, bad, very bad'. One could devise other metrics that would yield a continuous variable.


### 3.
