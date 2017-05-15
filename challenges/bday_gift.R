# B-day gift
# https://www.hackerrank.com/challenges/bday-gift

options(digits = 1)

nums <- suppressWarnings(read.table("/dev/stdin", sep="\n"))
nums <- nums$V1

price <- function(N, balls){
  if(N < 1 | N > 40) {
    stop("N must be between 1 and 40")
  }
  if(length(balls) != N) {
    stop("N doesn't equal number of items")
  }
  if(sum(balls < 1 | balls > 10^9) > 0) {
    stop("Balls must be between 1 and 10 ^ 9")
  }
  price0 <- 0.5 * sum(balls)
  price1 <- formatC(price0, digits = 1, format = "f")
  return(price1)
}

cat(price(nums[1], nums[2:length(nums)]))
