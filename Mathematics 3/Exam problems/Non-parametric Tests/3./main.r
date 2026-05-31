library(BSDA)


freq<-c(50,30,15,5)

#H0 X~GEO(0.8)
#HA X!~GEO(0.8)

p1<-dgeom(0,prob=0.8)
p2<-dgeom(1,prob=0.8)
p3<-dgeom(2,prob=0.8)
p4<-pgeom(3,prob=0.8,lower.tail=FALSE)+dgeom(3,prob=0.8)

probs<-c(p1,p2,p3,p4)

alpha<-0.05
result<-chisq.test(freq,p=probs)

freq
probs*100

#merge classes

pp1<-p1
pp2<-pgeom(1,prob=0.8,lower.tail=FALSE)+dgeom(1,prob=0.8)

freq<-c(50,50)
probs<-c(pp1,pp2)
result<-chisq.test(freq,p=probs)
result$p.value<alpha #TRUE

#Since the p-value is less than alpha we reject the null hypothesis.
#Conclusion:The data provides sufficient evidence to conclude that the distribution of X is not GEO(0.8).