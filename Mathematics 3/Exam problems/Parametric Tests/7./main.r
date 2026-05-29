library(BSDA)

x<-c(21, 20, 15, 19, 24, 25, 21, 19, 19 ,21)
y<-c(22, 26, 28, 22, 22, 25,21, 24, 24, 23, 27, 27, 23, 25, 22)

#H0:mu_x = mu_y
#HA mu_x < mu_y

alpha<-0.05

result<-t.test(x,y,alternative="less",conf.level=(1-alpha),var.equal=TRUE)
result$statistic #-3.675556
result$p.value #0.0006272451
result$p.value < alpha #TRUE

#Since the p-value is less than alpha,we reject the null hypothesis.
#Conclusion:There is enough evidence to support the claim that the new recipe is greater than the expected amount of protein in a meal prepared according to the current recipe....

#Alternative solution.
t.crit <- qt(alpha,df=(length(x)+length(y)-2),lower.tail=TRUE)
t.crit # -1.713872

#C(-infinity,-t.crit) t.test is in the critical region,so we reject the null hypothesis.