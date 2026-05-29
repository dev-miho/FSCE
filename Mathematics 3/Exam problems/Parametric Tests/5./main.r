library(BSDA)

x<-c(120, 125, 130, 110, 115, 140, 135, 128, 122, 118, 132, 140, 138, 121, 133, 130, 126, 127, 129, 119, 136, 125, 123, 131,
124, 137, 139, 120, 128, 132, 125, 100, 101, 102, 103)

alpha<-0.05

#H0:mu = 95
#HA:mu > 95

result<-z.test(x,mu=95,sigma.x=sqrt(var(x)),alternative="greater",conf.level=(1-alpha))
result$statistic #15.86284
result$p.value #0
result$p.value < alpha #TRUE

#Since the p-value is less than alpha,we reject the null hypothesis.
#Conclusion:There is enough evidence to support the claim that the expected weekly mass of purchased gold has increased as a result of the marketing campaign.

#Alternative solution.

z.crit<-qnorm(alpha,lower.tail=FALSE)
z.crit #1.644854
#C(z.crit, +infinity),z.test is in the critical region,so we reject the null hypothesis.