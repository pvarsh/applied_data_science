library(foreign)
library(car)

##### PROBLEM 1

### a. Read the data.
gril = read.dta("/Users/petervarshavsky/Documents/Git_NYU/applied_data_science/assignment_3/data/griliches.dta")

### b. Generate summary statistics (see Python code)

### c. Generate scatter plots (see Python code)

### d. Estimate bivariate linear regressions (see Python code)

### e. Estimate bivariate linear model of lw ~ schooling
mod1 = lm(lw~s, data = gril)
summary(mod1)
confint(mod1)

### f. Estimate a multivariate linear model of lw as a function of variables in (b)
cols = c('rns', 'mrt', 'smsa', 'med', 'iq', 'kww', 'age', 's', 'expr', 'lw')
gril1 = gril[cols]

mod2 = lm(lw ~ ., data = gril1)
summary(mod2)

# confidence interval
confint(mod2)[9, 1:2]


### g. adding age^2 and changing order
gril1$agesq = gril1$age^2
colNewOrder = c("rns","mrt","smsa", "med","iq", "kww", "age", "agesq", "s", "expr", "lw")
gril1 = gril1[, colNewOrder]

## linear regression with agesq
mod3 = lm(lw~., data = gril1)
summary(mod3)
confint(mod3)

## Plotting schooling vs age and age^2 to understand correlations
par(mfcol=c(1,2)) # 1 row 2 columns
par(mar=c(5,4,1,1)) # margins
plot(jitter(gril1$age, .8), jitter(gril1$s, .3), pch = 1, ylab = 'Years of schooling (s)', xlab = "Age (age)")
abline(lm(s~age, data = gril1), col = 'orange2', lwd = 2)
par(mar=c(5,3,1,2))
plot(jitter(gril1$agesq, 8), jitter(gril1$s, .3), pch = 1, ylab = '', xlab = "Age^2 (agesq)")
abline(lm(s~agesq, data = gril1), col = 'orange2', lwd = 2)
title("Age, age squared, and schooling", outer = T)

## Correlations of schooling, age, age^2
cor(gril1[c('s', 'age', 'agesq')])

###### Problem 2.
### a.
set.seed(12334)
x1 = rnorm(1e4)
x2 = rnorm(1e4)
epsilon = rnorm(1e4)
beta0 = 1
beta1 = 1
beta2 = 1
y = beta0 + beta1 * x1 + beta2 * x2 + epsilon

mod1 = lm(y~x1)
summary(mod1)
mod2 = lm(y~x1 + x2)
summary(mod2)

### b.
par(mfrow = c(1,1))
set.seed(12334)
z = rnorm(1e4)
v = rnorm(1e4, 0, 1)
w = rnorm(1e4, 0, 1)
x1 = z + v
x2 = -z + w
y = 1 + x1 + x2 + rnorm(1e4)

## using least squares fit
#mod1 = lsfit(x1, y)
#mod1$coef

## using lm
mod1 = lm(y~x1)
mod1$coef
summary(mod1)
#smpl = sample.int(1e4, size = 500)
#plot(x1[smpl], mod1$resid[smpl])
mod2 = lm(y~x1 + x2)
summary(mod2)
plot(x1, y)
abline(lm(y~x1), col = 'orange2', lwd = 3)
abline(h = mean(y), col = 'cyan2', lwd = 2)
#plot(x2, y)
#plot(x1, x2)

## Well behaved regression
x = rnorm(1e4)
y = 1 + x + rnorm(1e4)
mod1 = lsfit(x, y)
mod1$coef
plot(x, mod1$resid)
plot(y, mod1$resid)

########### PROBLEM 3
### a. Read data.
union = read.dta("/Users/petervarshavsky/Documents/Git_NYU/applied_data_science/assignment_3/data/union.dta")
### b.

## training set and test set
union.train = union[union$year >= 70 & union$year <= 78, ]
summary(union.train)
union.test = union[union$year < 70 | union$year > 78, ]
summary(union.test)

## linear model
lin.mod1 = lm(union ~ ., data = union.train)
summary(lin.mod1)

## logistic model
logit.mod1 = glm(union ~ ., data = union.train, family = binomial)
summary(logit.mod1)

### c. Predictions
threshold = 0.25
lin.prediction = predict(lin.mod1, newdata = union.test) >= threshold
logit.prediction = predict(logit.mod1, newdata = union.test, type = "response") >= threshold 

### d.

## Making and printing predictions
threshold = 0.2
lin.prediction = predict(lin.mod1, newdata = union.test) >= threshold
logit.prediction = predict(logit.mod1, newdata = union.test, type = "response") >= threshold 
cat("Actual union members:", sum(union.test$union))
cat("Predicted with linear probability model:", sum(lin.prediction))
cat("Predicted with logistic model:", sum(logit.prediction))

## Making and printing predictions
threshold = 0.25
lin.prediction = predict(lin.mod1, newdata = union.test) >= threshold
logit.prediction = predict(logit.mod1, newdata = union.test, type = "response") >= threshold 
cat("Actual union members:", sum(union.test$union))
cat("Predicted with linear probability model:", sum(lin.prediction))
cat("Predicted with logistic model:", sum(logit.prediction))

## Confusion matrices
cat("Confusion matrices")
table(lin.prediction, union.test$union)
table(logit.prediction, union.test$union)
