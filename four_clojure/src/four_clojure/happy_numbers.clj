(ns four-clojure.happy-numbers)

(defn next-happy-number
  [x]
  (let [digits (map #(Character/digit % 10) (seq (str x)))
        squares (map #(* % %) digits)]
    (reduce + squares)))

(defn is-hn-recur
  [x seen-nums]
  (let [next-hn (next-happy-number x)]
    (cond
      (seen-nums next-hn) false

      (= next-hn 1) true

      :else (is-hn-recur next-hn (conj seen-nums next-hn)))))

(defn is-happy-number?
  "problem 86
  recursively hn-next until we hit something that's already been hit OR we get to 1"
  [x]
  (is-hn-recur x (set [x])))
