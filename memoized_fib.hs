
memoized_fib :: Int -> Integer
memoized_fib = (map fib [0 ..] !!)
   where fib 0 = 0
         fib 1 = 1
         fib n = (memoized_fib (n-2) + memoized_fib (n-1)) `mod` (10^8+7)

routine 0 = return()
routine n = do
  x <- readLn :: IO Int
  print $ memoized_fib x
  routine (n-1)

main = do
  n <- readLn :: IO Int
  routine n
