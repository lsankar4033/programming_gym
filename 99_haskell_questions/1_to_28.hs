import System.Random
import Control.Monad (replicateM)

-- problem 1: last element of list
myLast :: [a] -> a
myLast [] = error "Can't find last element of empty list"
myLast [x] = x
myLast (_: xs) = myLast xs

-- problem 2: last but one element of list
myButLast :: [a] -> a
myButLast l
  | (length l) < 2 = error "Can't find second to last element of list of length < 2"
  | otherwise = myLast (init l)

-- problem 3: kth element of a list (1-indexed)
elementAt :: [a] -> Int -> a
elementAt [] n = error "list length must be >= n"
elementAt l 1 = head l
elementAt l n = elementAt (tail l) (n-1)

-- problem 4: num elements in list
myLength :: [a] -> Int
myLength [] = 0
myLength (x:xs) = 1 + (myLength xs)

-- problem 5: reverse a list
myReverse :: [a] -> [a]
myReverse [] = []
myReverse (x:xs) = (myReverse xs)++[x]

-- problem 6: determine if list is palindrome
isPalindrome :: (Eq a) => [a] -> Bool
isPalindrome [] = True
isPalindrome [_] = True
isPalindrome xs = (head xs) == (myLast xs) && isPalindrome ((tail . init) xs)

-- problem 7: flatten a nested list structure
data NestedList a = Elem a | List [NestedList a]

flatten :: NestedList a -> [a]
flatten (Elem a) = [a]
flatten (List (x:xs)) = flatten x ++ flatten (List xs)
flatten (List []) = []

-- problem 8: eliminate consecutive duplicates
compress :: (Eq a) => [a] -> [a]
compress [] = []
compress [x] = [x]
compress (x1:(x2:xs))
  | x1 == x2 = compress (x1:xs)
  | otherwise = (x1:compress (x2:xs))

-- problem 9: pack consecutive duplicates into sublists
pack :: (Eq a) => [a] -> [[a]]
pack [] = []
pack (x:xs) = let (xGrp, rest) = span (==x) xs
               in (x:xGrp) : (pack rest)

-- problem 10: run-length encoding
encode :: (Eq a) => [a] -> [(Int, a)]
encode l = map (\x -> (length x, head x)) (pack l)

-- problem 11: modified run-length encoding
data EncodingItem a = Multiple Int a | Single a
  deriving (Show)

encodeModified :: (Eq a) => [a] -> [EncodingItem a]
encodeModified = map modify . encode
  where
    modify (1,x) = Single x
    modify (n,x) = Multiple n x

-- problem 12: (modified) run-length decoding
decodeModified :: (Eq a) => [EncodingItem a] -> [a]
decodeModified = concatMap expand
  where
    expand (Single x) = [x]
    expand (Multiple n x) = take n $ repeat x

-- problem 13: direct run-length encoding
encodeDirect :: (Eq a) => [a] -> [EncodingItem a]
encodeDirect [] = []
encodeDirect (x:xs)
  | dupCount == 1 = Single x : encodeDirect xs
  | otherwise = Multiple dupCount x : encodeDirect rest
    where
      (dups, rest) = span (==x) (x:xs)
      dupCount = (length dups)

-- problem 14: duplicate each element in list
dupli :: [a] -> [a]
dupli [] = []
dupli (x:xs) = [x,x] ++ (dupli xs)

-- problem 15: replicate each element in a list N times
repli :: [a] -> Int -> [a]
repli [] _ = []
repli (x:xs) n = (take n $ repeat x) ++ (repli xs n)

-- problem 16: drop every nth element from list
dropEvery :: [a] -> Int -> [a]
dropEvery xs n = inner xs n n
  where
    inner [] _ _ = []
    inner (x:xs) n 1 = inner xs n n
    inner (x:xs) n m = x : (inner xs n (m - 1))

-- problem 17: split into two parts, length of first part given
split :: [a] -> Int -> ([a], [a])
split xs n = (take n xs, drop n xs)

-- problem 18: extract a slice from a list
slice :: [a] -> Int -> Int -> [a]
slice xs n m
  | n > 0 && m > 0 = take (m-n+1) $ drop (n-1) xs
  | otherwise = error "Neither slice index can be < 1"

-- problem 19: rotate N places to left
rotate :: [a] -> Int -> [a]
rotate xs n = (drop modlen xs) ++ (take modlen xs)
  where
    modlen = mod n (length xs)

-- problem 20: remove the kth element
removeAt :: Int -> [a] -> (a, [a])
removeAt i xs = (xs !! (i-1), (take (i-1) xs) ++ (drop i xs))

-- problem 21: insert element at a given position
insertAt :: a -> [a] -> Int -> [a]
insertAt x xs i
  | (length xs) < i - 1 = error "position too big"
  | i < 1 = error "positions < 1 not allowed"
  | otherwise = (take (i-1) xs) ++ (x:drop (i-1) xs)

-- problem 22: range (trivially [a..b], but I wanted to challenge myself)
range :: Int -> Int -> [Int]
range a b = take (b-a+1) $ iterate (+1) a

-- problem 23: extract N random numbers
rndSelect :: [a] -> Int -> IO [a]
rndSelect [] _ = error "can't select elements from an empty list"
rndSelect xs n = do
  indices <- replicateM n (randomRIO (0, (length xs) - 1) :: IO Int)
  return [xs !! i | i <- indices]

-- problem 24: draw N distinct random numbers from the range 1..M
diffSelect :: Int -> Int -> IO [Int]
diffSelect n m
  | n > m = error "n can't be greater than m"
  | otherwise = diffSelect' n [1..m]

-- recursively select n
diffSelect' :: Int -> [Int] -> IO [Int]
diffSelect' 0 _ = return []
diffSelect' _ [] = error "can't select elements from an empty list"
diffSelect' n xs = do
  curInd <- randomRIO (0, (length xs) - 1)
  let remaining = (take curInd xs) ++ (drop (curInd + 1) xs)
  rest <- diffSelect' (n - 1) remaining
  return ((xs !! curInd) : rest)

-- problem 25: random permutation of elements in list
rndPermu :: [a] -> IO [a]
rndPermu xs = do
  perm <- diffSelect (length xs) (length xs)
  return [xs !! (i-1) | i <- perm]

-- problem 26: generate all combinations
comb :: Int -> [a] -> [[a]]
comb 0 _ = [[]]
comb n xs = [xs !! i : ys | i <- [0..(length xs)-1],
                            ys <- comb (n-1) (drop (i+1) xs)]

-- problem 27: disjoint subset grouping

