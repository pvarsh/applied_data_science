#install.packages("neuralnet")
#library(neuralnet)

set.seed(123)
k = 300
x = seq(0, 20, length.out=k)
y = sin(x) + rnorm(k, 0, .5)
df = cbind(x, y)
plot(x, y, pch = 19, cex = 0.1)

nnet1 = neuralnet(y~x, data = df, hidden = 2)

pred.net = prediction(nnet1)
str(pred.net)
y.pred = pred.net$rep1[,2]
lines(x, y.pred)
