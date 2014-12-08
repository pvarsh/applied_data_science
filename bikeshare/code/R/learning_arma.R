install.packages("tseries")
library(tseries)
### Generate a sin wave
pi
### Create x
x = seq(0, 8*pi, length = 200)
### Create y
y = sin(x) + rnorm(length(x), 0, 0.3)
### Plot time series
plot.ts(y)
### arma models
arma.1 = arma(y, order = c(6,0))

yNA = y
yNA[20:30] = NA
yNA[50:60] = NA
yNA[80:90] = NA
yNA[110:120] = NA
yNA[140:150] = NA
yNA[170:180] = NA

plot.ts(yNA)
arma.2 = arma(y, order = c(6,0))
summary(arma.2)
