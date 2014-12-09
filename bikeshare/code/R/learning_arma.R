#install.packages("tseries")
#library(tseries)
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
yNA[20:23] = NA
yNA[50:53] = NA
yNA[80:83] = NA
yNA[110:113] = NA
yNA[140:143] = NA
yNA[170:173] = NA

plot.ts(yNA)
arma.2 = arma(y, order = c(6,0))
summary(arma.2)


### From http://www.statoek.wiso.uni-goettingen.de/veranstaltungen/zeitreihen/sommer03/ts_r_intro.pdf
### Page 17
sim.ar<-arima.sim(list(ar=c(0.4,0.4)),n=1000)
sim.ma<-arima.sim(list(ma=c(0.6,-0.4)),n=1000)
par(mfrow=c(2,2))
acf(sim.ar,main="ACF of AR(2) process")
acf(sim.ma,main="ACF of MA(2) process")
pacf(sim.ar,main="PACF of AR(2) process")
pacf(sim.ma,main="PACF of MA(2) process")

plot(sim.ma)
