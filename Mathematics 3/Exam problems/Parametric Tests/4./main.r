library(BSDA)


x<-c(82, 75, 88, 79, 81, 85, 77, 80, 83, 78, 79)
y<-c(79, 81, 76, 84, 80, 78, 82, 77, 83, 79)

alpha<-0.05
#H0:mu_x = mu_y
#HA:mu_x != mu_y

result<-t.test(x,y,alternative="two.sided",conf.level=(1-alpha),var.equal=TRUE)
result$statistic  #0.5201682 
result$p.value #0.6089547
result$p.value < alpha #FALSE

#Since the p-value is greater than alpha,we do not reject the null hypothesis.
#Conclusion:There is not enough evidence to support the expected results of students in the two groups differ.

#Alternative solution.
t.crit <-qt(alpha/2,df=length(x)+length(y)-2,lower.tail=FALSE)
t.crit #2.093024

#C(-infinity, -t.crit) U (t.crit, +infinity),t.test is not in the critical region,so we do not reject the null hypothesis.