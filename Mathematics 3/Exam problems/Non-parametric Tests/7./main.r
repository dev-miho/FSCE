library(BSDA)

table<-matrix(c(60,10,0,30,10,10,0,10,20),nrow=3,ncol=3,byrow=TRUE)

alpha <- 0.01

result<- chisq.test(table, correct=FALSE)
result$statistic
result$p.value<alpha #TRUE

#Since the p-value is less than the significance level, we reject the null hypothesis. 

#Conclusion: There is a significant association between cost and artificial intelligence index.