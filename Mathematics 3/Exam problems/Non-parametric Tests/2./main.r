library(BSDA)

table<-matrix(c(14,48,20,16,55,6),nrow=2,ncol=3,byrow=TRUE)

table

#Let X be attribute "Gender" and Y be attribute "Personal income level"

#H0:X and Y are independent
#HA:X and Y are not independent

alpha<-0.05

result<-chisq.test(table,correct=FALSE)
result$p.value<alpha

#Since the p-value is less than alpha we reject the null hypothesis.
#Conclusion:There is not enough evidence to conclude that X and Y are independent.

