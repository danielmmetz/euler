answer = sum [x | x <- [1..1000], or [x `mod` 3 == 0, x `mod` 5 == 0]]

main = putStrLn $ show answer

