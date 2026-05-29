library(BSDA)

x<-c(5310, 6690, 7388, 6253, 5319, 7660, 7834, 8084, 6676, 6903, 7148, 7532,
6426, 7655, 7220, 6370, 6671, 7097, 8829, 8748, 8692, 7237, 6041, 6575,
6252)

sigma=900

mu=7200

alpha=0.01

#H0:mu = 7200
#HA:mu < 7200

result<-z.test(x,mu=mu,sigma.x=sigma,alternative="less",conf.level=(1-alpha))

result$statistic # −0.7533333
result$p.value # 0.2256248
result$p.value< alpha #FALSE

#Since the p-value is greater than alpha,we do not reject the null hypothesis.
#Conclusion:There is not enough evidence to support the claim that average number of steps per day for person is less than 7200.

#Alternative solution.

z.crit <- qnorm(alpha,lower.tail=TRUE)
z.crit # -2.326348

#C(-infinity,-z.crit) z.test is not in the critical region,so we do not reject the null hypothesis.