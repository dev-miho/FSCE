library(BSDA)




x<-c(743, 751, 748, 757, 752, 745, 750, 755, 749, 754, 742, 756, 744, 753, 746)

sigma <- 2

alpha<-0.05

#H0:sigma=2
#HA:sigma>2

result<-((length(x)-1)*var(x))/(sigma^2)
result #83.833333

chi.crit<-qchisq(alpha,df=length(x)-1,lower.tail=FALSE)
chi.crit #23.68479

result < chi.crit
#C(chi.crit, +infinity),result is in the critical region,so we reject the null hypothesis.
#Conclucion:There is enough evidence to support the claim that standard deviation in the packages is greater than 2