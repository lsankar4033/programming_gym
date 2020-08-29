module Lib
    ( someFunc
    ) where

reverseWords :: String -> String
reverseWords = unwords . map reverse . words

someFunc :: IO ()
someFunc = do
  line <- getLine
  if null line
    then return ()
    else do
      putStrLn $ reverseWords line
