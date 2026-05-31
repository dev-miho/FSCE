library(BSDA)

p0 <- pgeom(1,0.3)
p1 <- dgeom(2,0.3)
p2 <- dgeom(3,0.3)
p3 <- dgeom(4,0.3)+pgeom(4,0.3,lower.tail=FALSE)

alpha<-0.05

freqs <- c(20,45,20,15)

probs <- c(p0,p1,p2,p3)

#H0: The data follows the geometric distribution with parameter 0.3.
#H1: The data does not follow the geometric distribution with parameter 0.3.

result<-chisq.test(freqs,p=probs)

result$statistic #93,84203

result$p.value

result$p.value < alpha #TRUE

#Since the p-value is less than the significance level, we reject the null hypothesis.
#Conclusion: The data does not follow the geometric distribution with parameter 0.3.

