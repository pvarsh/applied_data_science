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

###### OUTLIERS
summary(traff.df)

## plot histograms
df.hist(traff.df)


###### PREDICTING ADULT VICTIMS



###### PREDICTING CHILD VICTIMS

###### PREDICTING PROSECUTIONS
