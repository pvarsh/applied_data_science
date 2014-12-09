#install.packages('forecast')
#library(forecast)

par(mfrow=c(1,1))

### generate moving average model
x = seq(0, 8*pi, len = 400)
plot(x)
y = sin(x) + 0.5*cos(4*x) + rnorm(length(x), 0, 0.5) + 0.1*x
y[90:100] = NA
y[190:200] = NA
y[290:300] = NA
z = sin(x)
plot(y, type = 'l')

###
mod1 = Arima(y, order = c(1, 1, 1))
#tsdiag(mod1)
#summary(mod1)

plot(mod1$x, type = 'l')
lines(fitted(mod1), col = 'cyan')


pacf(y)
summary(mod1)

