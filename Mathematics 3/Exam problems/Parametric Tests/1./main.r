library(BSDA)

#H0:mu = 69
#HA:mu != 69

x<-c(68, 65, 68, 72, 68, 75, 70, 72, 70, 72, 65, 83, 72, 68, 72, 70, 65, 70, 70, 70, 75)

sigma=4

mu=69

alpha=0.05

result<-z.test(x,mu=mu,sigma.x=sigma,alternative='two.sided',conf.level=(1-alpha))

result$statistic
result$p.value

result$p.value < alpha

#Since the p-value is greater than alpha,we do not reject the null hypothesis.
#Conclusion:There is not enough evidence to support the claim that average heart rate of this group differs from the previously reported average of 69 bpm.

#Alternative solution.

z.crit <- qnorm(alpha/2,lower.tail=FALSE)
z.crit

#C(-infinity, -z.crit) U (z.crit, +infinity),z.test is not in the critical region,so we do not reject the null hypothesis.