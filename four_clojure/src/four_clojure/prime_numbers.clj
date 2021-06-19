(ns four-clojure.prime-numbers)

(defn is-prime? [n]
  (if (< n 3)
    (= n 2)
    (let [highest-div (int (Math/sqrt n))
          divisors (filter #(= 0 (mod n %))
                           (range 2 (inc highest-div)))]
      (empty? divisors))))

(defn next-prime
  "keep going beyond cur and find the next prime"
  [cur]
  (first
   (filter is-prime? (iterate inc (inc cur)))))

(defn primes
  "problem 67

  Returns the first n prime integers"
  [n]
  (reduce
   (fn [primes _]
     (conj
      primes
      (next-prime (last primes))))
   [2]
   (range (dec n))))
