library(BSDA)

print("a)")
x<-rbinom(n=30,size=900,prob=0.7)

print("b)")
mean(x)
var(x)
sd(x)
guartiles<-quantile(x,probs=c(0.25,0.75))
q1<-guartiles[1]
q3<-guartiles[2]
IQR(x)
hist(x)

print("c)")