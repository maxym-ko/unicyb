# dataset source: https://www.kaggle.com/tombutton/body-measurements
dataset <- read.csv("/home/maxym_ko/cyb/cyb_r/lab_2/measures.csv", header=TRUE)

weight <- dataset$weight * 0.453592 # convert from lb to kg
chest <- dataset$chest
abdom <- dataset$abdom
fat <- dataset$brozek

pairs(list(weight, abdom, chest, fat), col = 6, 
      labels = list("Weight", "Abdominal", "Chest", "Body fat"))

model <- lm(fat ~ weight + abdom + chest)
summary(model)

model <- lm(fat ~ weight + abdom)
summary(model)

# check residuals for normality distribution
qqnorm(model$residuals, ylab = "Residuals Quantiles")
qqline(model$residuals, col = 'red')

# check residuals and predicted values for independence
plot(model$fitted.values, model$residuals, col=6,
     xlab = "Predicted fat values", ylab = "Residuals")

