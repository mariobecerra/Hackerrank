# normal distribution 3
# https://www.hackerrank.com/challenges/normal-distribution-3

a <- 100 * (1 - pnorm((80 - 70)/10))
b <- 100 * (1 - pnorm((60 - 70)/10))
c <- 100 - b

cat(formatC(a, digits = 2, format = "f"), "\n")
cat(formatC(b, digits = 2, format = "f"), "\n")
cat(formatC(c, digits = 2, format = "f"), "\n")
