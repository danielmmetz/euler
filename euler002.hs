fibs = 0 : 1 : zipWith (+) fibs (tail fibs)
isEven n = n `mod` 2 == 0

answer = sum $ takeWhile (< 4000000) [x | x <- filter isEven fibs]

main = putStrLn $ show answer
