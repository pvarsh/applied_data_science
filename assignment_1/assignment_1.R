
# Numbers from random.org
x = c(6,3,6,8,1,3,8,4,9,1)
y = c(0,5,3,0,0,6,5,9,3,8)

### Problem 1

# a.
plot(x, y)
# b.
mean(x)
mean(y)
# c.
var(x)
var(y)
# d.
sd(x)
sd(y)
# e.
cov(x,y)
# f.
cor(x,y)
# g.


a = 1:10
b = a*0.5 + 2
c = a * 3 - 1
plot(a,b)
plot(a,c)
points(a,b)
cov(a,b)
cov(a,c)
cor(a,b)
cor(a,c)

### 2.
# a. Discrete. The number of rides taken by a resident in a month is a count variable that takes values on the set of natural numbers, which is discrete.
# b. Continuous. Bicyclist's speed can take any real value bounded from below by 0 and from above by the speed of light. No particular value of speed has probabily mass, only density.
# c. Continuous. Minute variations in lamps and current suggest a continuous variable. If the minute variations are not of interest, then the luminosity measurements can be converted to a discrete variable.
# d. Discrete. Assuming bankers cannot receive arbitrarily small fractions of a dollar, the salaries are discrete, however a continuous variable may be more convenient.
# e. Discrete. The number of hotels in Manhattan is a count variable.
# f. Continuous. Loudness is continuous.
# g. Discrete. Coffee can be 'good or bad' or 'very good, good, average, bad, very bad'. One could devise other metrics that would yield a continuous variable.

### 3. 