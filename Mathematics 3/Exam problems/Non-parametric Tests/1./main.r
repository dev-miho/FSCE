library(BSDA)

#H0:X~B(20,0.1)
#H1:X!~B(20,0.2)

freq<-c(54,25,10,11)
p0<-dbinom(0,size=20,prob=0.1)
p1<-dbinom(1,size=20,prob=0.1)
p2<-dbinom(2,size=20,prob=0.1)


p3<-dbinom(3,size=20,prob=0.1)+pbinom(3,size=20,prob=0.1,lower.tail=FALSE)

probs<-c(p0,p1,p2,p3)

alpha<-0.05
result<-chisq.test(freq,p=probs,conf.level=(1-alpha))
result$p.value<alpha #TRUE

#Since the p-value is less than alpha we reject the null hypothesis.
#Conclusion:The data provides sufficient evidence to conclude that the distribution of X is not B(20,0.1).