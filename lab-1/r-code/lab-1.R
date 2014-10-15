### CLEAR
rm(list = ls())

### LIBRARIES

### FUNCTIONS
df.hist = function(df, columns = F){
  if (columns != F){
    for (i in columns){
      hist(df[ ,i], main = colnames(df)[i])
    }
  }
  else {
    len = dim(df)[2]
    for (i in 1:len){
      if (is.numeric(df[ ,i])){
        hist(df[ ,i], main = colnames(df)[i])
      }
    }
  }
}

compareLogTransforms = function(countries, y, x){

  log.x = log(x)
  log.y = log(y)
  infinities = log.x == -Inf | log.y == -Inf
  trans.df = data.frame(x = log.x[!infinities], y = log.y[!infinities])
  plot(x, y, main = "y against x")
  plot(trans.df$x, trans.df$y, main = "log(y) against log(x)")
  linmod = lm(log.y[!infinities] ~ log.x[!infinities])
  abline(linmod, col = 'red')
  print(cat("\nP-value", summary(linmod)$coefficients[2, 4]), sep = " ")
  
  return(trans.df)
}

compareLogTransforms1 = function(df, xcol, ycol){
  
  log.df = df[,c(1, xcol, ycol)]
  print(head(log.df))
  exclude = log.df[2] == -Inf | log.df[3] == -Inf | log.df[2] == NaN | log.df[3] == NaN
  cat("Excluded ", sum(exclude), " rows")
  
#   infinities = log.x == -Inf | log.y == -Inf
#   trans.df = data.frame(x = log.x[!infinities], y = log.y[!infinities])
#   plot(x, y, main = "y against x")
#   plot(trans.df$x, trans.df$y, main = "log(y) against log(x)")
#   linmod = lm(log.y[!infinities] ~ log.x[!infinities])
#   abline(linmod, col = 'red')
#   print(cat("\nP-value", summary(linmod)$coefficients[2, 4]), sep = " ")
#   return(trans.df)

}
a = compareLogTransforms1(traff.df.outRem1, xcol = 7, ycol = 10)


###### READ DATA

## file paths
data.path = "/Users/petervarshavsky/Documents/Git_NYU/applied_data_science/lab-1/data/"
traff.data.file = paste0(data.path, "trafficking_data.csv")
new.data.file = paste0(data.path, "new.csv")

## read files
traff.df = read.csv(traff.data.file, header = TRUE, sep = ",", stringsAsFactors = F)
new.df = read.csv(new.data.file, header = TRUE, sep = ",", stringsAsFactors = F)

###### CLEAN UP
## column names
colnames(traff.df) = tolower(colnames(traff.df))
## countries as factor
traff.df$country = as.factor(traff.df$country)
## compute all victims
traff.df$total.victims = traff.df$child.victims + traff.df$adult.victims

###### OUTLIERS
summary(traff.df)

## plot histograms
df.hist(traff.df)


###### PREDICTING ADULT VICTIMS
names(traff.df)

mod1.1 = lm(total.victims ~ . - child.victims - adult.victims, data = traff.df)
sum1.1 = summary(mod1.1)
print(sum1.1)

mod1.2 = lm(total.victims ~ . - child.victims - adult.victims - country, data = traff.df)
sum1.2 = summary(mod1.2)
print(sum1.2)

# The model using all predictors of total victims shows no significance except for country names.
# No variables have predictive power.

### Removing outlying countries by persons.prosecuted
outlier.cutoff = 10000
traff.df.outRem1 = traff.df[traff.df$persons.prosecuted < outlier.cutoff, ]  #outlier Removed

mod2.1 = lm(total.victims ~ . -child.victims - adult.victims, data = traff.df.outRem1)
sum2.1 = summary(mod2.1)
print(sum2.1)

mod2.2 = lm(total.victims ~ . -child.victims - adult.victims - country, data = traff.df.outRem1)
sum2.2 = summary(mod2.2)
print(sum2.2)

### Log scale each predictor

# gdp
traff.df.outRem1$log.gdp = log(traff.df.outRem1$gdp)
traff.df.outRem1[traff.df.outRem1$log.gdp < 0, c(1, 10)] # checking for what countries and values of total.victims log.gdp is negative
traff.df.outRem2 = traff.df.outRem1[traff.df.outRem1$log.gdp > 0, ] # removing negative log.gdp
log(traff.df.outRem2$total.victims), traff.df.outRem2$log.gdp

# persons prosecuted
traff.df.outRem1$log.persons.prosecuted = log(traff.df.outRem1$persons.prosecuted)
plot(log(traff.df.outRem1$total.victims), log(traff.df.outRem1$persons.prosecuted)) # log - log has a linear trend

# total.victims
traff.df.outRem1$log.total.victims = log(traff.df.outRem1$total.victims)
summary(lm(log.total.victims ~ log.gdp, data = traff.df.outRem1))

mod3.1 = lm(total.victims ~ log.gdp +
              year + persons.prosecuted +
              policy.index +
              x..females.in.primary.education +
              life.expectancy,
            data = traff.df.outRem2)

summary(mod3.1)

colnames(traff.df.outRem2)
plot(traff.df.outRem2)

## GDP colored by Country plot
plot(traff.df.outRem2$log.gdp, col = traff.df.outRem2$country)
plot(traff.df.outRem2$log.gdp, traff.df.outRem2$year, col = traff.df.outRem2$country)

a = compareLogTransforms(traff.df.outRem1$country, traff.df.outRem1$gdp, traff.df.outRem1$total.victims)
a = compareLogTransforms1(traff.df.outRem1, xcol = 7, ycol = 10)


###### PREDICTING CHILD VICTIMS

###### PREDICTING PROSECUTIONS
