library(BSDA)

x <- c(21, 20, 15, 19, 24, 25, 21, 19, 19, 21)
y <- c(22, 26, 28, 22, 22, 25, 21, 24, 24, 23, 27, 27, 23, 25, 22)

alpha <- 0.05

# H0: sigma_x = sigma_y
# HA: sigma_x > sigma_y

result <- var.test(x, y, alternative = "greater", conf.level = (1 - alpha))
result$statistic # 1.636122
result$p.value # 0.1972086
result$p.value < alpha # FALSE

# Since the p-value is greater than alpha,we do not reject the null hypothesis.
# Conclusion:There is not enough evidence to support the claim that the variance of the amount of protein in a meal prepared using the new recipe is smaller than the variance of the amount of protein in a meal prepared using the current recipe.

# Alternative solution.

f.crit <- qf(alpha, df1 = length(x) - 1, df2 = length(y) - 1, lower.tail = FALSE)
f.crit # 2.645791
# C(f.crit, +infinity),f.test is not in the critical region,so we do not reject the null hypothesis.
