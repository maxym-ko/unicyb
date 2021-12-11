# attach(population_dataset)

options(warn=-1)

library('e1071')
library('outliers')

# dataset source: https://www.kaggle.com/tanuprabhu/population-by-country-2020
dataset <- read.csv("/home/maxym_ko/cyb/cyb_r/lab_1/population_dataset.csv", header=TRUE)

population <- as.double(dataset$population)
area <- as.double(dataset$area)
migrants_net <- as.double(dataset$migrants_net)
age_med <- as.double(dataset$age_med)

remove_outliers <- function(x, na.rm = TRUE, ...) {
  qnt <- quantile(x, probs=c(.25, .75), na.rm = na.rm, ...)
  H <- 1.5 * IQR(x, na.rm = na.rm)
  y <- x
  y[x < (qnt[1] - H)] <- NA
  y[x > (qnt[2] + H)] <- NA
  y
}

analysis <- function(data_vector, data_name) {
  data_vector <- data_vector[!is.na(data_vector)]
  
  par(mfrow = c(3, 1), mgp = c(1.5, 0.8, 0))
  
  # Frequency polygon
  hist(data_vector, 
       main = paste("Frequency polygon of ", data_name),
       xlab=data_name,
       col = "Steelblue3")
  
  # Probability density function
  plot(main = paste("Probability density function of ", data_name),
       xlab = data_name,
       density(data_vector))
  
  # Box plot
  boxplot(data_vector, 
          main = paste("Box plot of ", data_name),
          xlab = data_name,
          horizontal = TRUE)
  
  # Basic characteristics
  print(paste("Min of ", data_name, ":", min(data_vector)))
  print(paste("Max of ", data_name, ":", max(data_vector)))
  print(paste("Median of ", data_name, ":", median(data_vector)))
  
  print(paste("Quantile of ", data_name, ":"))
  print(quantile(data_vector))
  
  print(paste("Decile of ", data_name, ":"))
  print(quantile(data_vector, probs = seq(.1, .9, by = .1)))
  
  # Position characteristics
  print(paste("Expected value of ", data_name, ":", 
              mean(data_vector)))
  print(paste("Geometric mean of ", data_name, ":", 
              exp(mean(log(data_vector)[data_vector != 0])))) ## to handle negative values
  print(paste("Harmonic mean of ", data_name, ":", 
              1 / mean(1 / data_vector[data_vector != 0])))
  
  uniqv <- unique(data_vector)
  print(paste("Mode value of ", data_name, ":", 
              uniqv[which.max(tabulate(match(data_vector, uniqv)))]))
  
  print(paste("Median value of ", data_name, ":", 
              median(data_vector)))
  
  # Deviation characteristics
  print(paste("Variance value of ", data_name, ":", 
              var(data_vector)))
  print(paste("Root mean square of ", data_name, ":", 
              sqrt(mean(data_vector ^ 2))))
  print(paste("Coefficient of variation of ", data_name, ":", 
              sd(data_vector) / mean(data_vector) * 100))
  print(paste("Range of ", data_name, ":", 
              range(data_vector)[2]))
  print(paste("Distribution concentration interval of ", data_name, ": (", 
              mean(data_vector) - 3 * sqrt(var(data_vector)), ", ",
              mean(data_vector) + 3 * sqrt(var(data_vector)), ")"))
  
  # Symmetric distribution analysis
  beta_1 <- skewness(data_vector)
  if (beta_1 == 0) {
    skew <- "Symmetric"
  } else if (beta_1 > 0) {
    skew <- "Positive skew"
  } else {
    skew <- "Negative skew"
  }
  print(paste("Skewness of ", data_name, ":", beta_1, "[", skew, "]"))
  
  # Sharpness distribution analysis
  beta_2 <- kurtosis(data_vector)
  if (beta_2 == 0) {
    kurt <- "The same as normal distribution"
  } else if (beta_2 > 0) {
    kurt <- "More sharpness that normal distribution"
  } else {
    kurt <- "Less sharpness that normal distribution"
  }
  print(paste("Kurtosis of ", data_name, ":", beta_2, "[", kurt, "]"))
}

print("Starting analysis...")

analysis(population / 10e6, "Population (in millions)")
analysis(area, "Area (in thousands)")
analysis(age_med, "Age median")
analysis(migrants_net / 10e3, "Migrants (in thousands)")


# Removing outliers
population <- remove_outliers(population)
area <- remove_outliers(area)
migrants_net <- remove_outliers(migrants_net)
age_med <- remove_outliers(age_med)

analysis(population / 10e6, "Population (in millions)")
analysis(area, "Area (in thousands)")
analysis(age_med, "Age median")
analysis(migrants_net / 10e3, "Migrants (in thousands)")

# Correlation between Population and Area
cor.test(population, area, method = "pearson")

# Correlation between Age media and Migrants
cor.test(age_med, migrants_net, method = "pearson")

# Correlation between Population and Age median
cor.test(population, age_med, method = "pearson")

# Correlation between Area and Age median
cor.test(area, age_med, method = "pearson")


# Correlation between Population and {Area, Age median, Migrants}
xPopulation <- lm(population~area+age_med+migrants_net)
cor.test(xPopulation$model$population, xPopulation$fitted.values)

# Correlation between Area and {Population, Age median, Migrants}
xArea <- lm(area~population+age_med+migrants_net)
cor.test(xArea$model$area, xArea$fitted.values)

# Correlation between Age median and {Area, Population, Migrants}
xAge <- lm(age_med~population+area+migrants_net)
cor.test(xAge$model$age_med, xAge$fitted.values)

# Correlation between Migrants and {Area, Age median, Population}
xMigrants <- lm(migrants_net~population+area+age_med)
cor.test(xMigrants$model$migrants_net, xMigrants$fitted.values)
