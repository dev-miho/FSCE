library(BSDA)

x<-c(78, 82, 75, 80, 79, 81, 84, 77, 80, 78, 83, 79)
y<-c(76, 74, 79, 77, 75, 80, 73, 78, 76, 74, 81, 75, 77, 76, 79)

#H0:mu_x = mu_y
#HA:mu_x != mu_y
alpha<-0.01

result<-t.test(x,y,alternative="two.sided",conf.level=(1-alpha),var.equal=TRUE)

result$statistic #3.162278 
result$p.value #0.004075221
result$p.value < alpha #TRUE

#Since the p-value is less than alpha,we reject the null hypothesis.
#Conclusion:There is enough evidence to support the claim  that the expected yield of apple trees in Resen differs from the expected yield of apple trees in Tetovo

#Alternative solution.

t.crit <- qt(alpha/2,df=(length(x)+length(y)-2),lower.tail=FALSE)
t.crit # 2.787436

#C(-infinity, -t.crit) U (t.crit, +infinity),t.test is in the critical region,so we reject the null hypothesis.