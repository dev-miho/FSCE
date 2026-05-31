library(BSDA)

n <- 15
x <- c(2 , 5 , 3 , 4 , 1)
nll <- function (p) {
return ( -sum ( log ( dbinom (x , size = n , prob = p )) ))
}
result <- mle ( nll , start = 0.5 , lower = 0.001 , upper = 0.999)
result