library(BSDA)

x <-c (775,760,745,740,738)

sigma <- 5

alpha <- 0.05

mu=750

#H0: mu = 750
#H1: mu !< 750

result <-z.test(x,sigma.x=sigma,mu=mu,alternative="two.sided",conf.level=1-alpha)

result$statistic #0.7155418

result$p.value #0.4742744

result$p.value < alpha #FALSE

#Since the p-value is greater than the significance level, we fail to reject the null hypothesis.
#Conclusion: There is not enough evidence to conclude that the mean is different from 750.

