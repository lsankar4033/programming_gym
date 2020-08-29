import Data.List (group)

-- problem 31: determine if a number is prime
isPrime :: Integral a => a -> Bool
isqrt :: Integral a => a -> a

isqrt = floor . sqrt . fromIntegral
isPrime n = null [x | x <- [2..(isqrt n)], n `rem` x  == 0]

-- problem 32: gcd
myGCD :: Integer -> Integer -> Integer
myGCD a b
  | b == 0 = abs a
  | otherwise = myGCD b (a `mod` b)

-- problem 33: determine whether two integers are coprime
coprime :: Integer -> Integer -> Bool
coprime a b = myGCD a b == 1

-- problem 34: Euler's totient
totientPhi 1 = 1
totientPhi n = length $ filter (coprime n) [1..(n - 1)]

-- problem 35: prime factorization
primeFactors :: Integral a => a -> [a]
primeFactorsInner :: Integral a => a -> [a] -> [a]

-- uses accumulator to build up prime factors
primeFactorsInner 1 existing = existing
primeFactorsInner n existing
  = let start = if length existing == 0
                then 2
                else last existing
        nextPF = head [x | x <- [start..n], n `rem` x == 0]
    in primeFactorsInner (quot n nextPF) (existing ++ [nextPF])

primeFactors n = primeFactorsInner n []

-- problem 36: prime factors with multiplicity
primeFactorsMult n = map (sequence [head, length]) $ group pf
  where pf = primeFactors n

-- problem 37: Euler's totient improved
totientPhiImp n = foldl comb 1 pfm
  where pfm = primeFactorsMult n
        comb acc pm = acc * (p - 1) * (p ^ (m - 1))
          where p = pm !! 0
                m = pm !! 1


-- problem 39: all primes in range
primesR :: Integral a => a -> a -> [a]
primesR l h = filter isPrime [l..h]

-- problem 40: Goldbach's conjecture
goldbach :: Integral a => a -> (a, a)
goldbach n = head [(x, y) | x <- pr, y <- pr, x + y == n]
  where pr = primesR 2 n

-- problem 41: Goldbach List
goldbachList :: Integral a => a -> a -> [(a, a)]
goldbachListMV :: Integral a => a -> a -> a -> [(a, a)]

goldbachList l h = map goldbach evens
  where evens = [x | x <- [4..h], x `mod` 2 == 0]

goldbachListMV l h mv = filter (\x -> (fst x) > mv && (snd x) > mv) $ goldbachList l h
