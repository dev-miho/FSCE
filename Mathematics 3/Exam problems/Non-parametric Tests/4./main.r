
library(BSDA)

observed<-c(270,140,65,25)

ratios<-c(10,6,3,1)

probabilities<-ratios/sum(ratios)

alpha<-0.05

#H0:The distribution of heroes follows the ratio 10:6:3:1
#HA:The distribution of heroes does NOT follow the ratio 10:6:3:1

result<- chisq.test(x=observed,p=probabilities)

result$statistic #3.6

result$p.value< alpha #FALSE

#Since the p-value is greater than alpha,we do not reject the null hypothesis.
#Conclusion:There is not enough evidence to suggest that the distribution of heroes does not follow the ratio 10:6:3:1.