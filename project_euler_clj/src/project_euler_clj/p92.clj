(ns project-euler-clj.p92)



; take iteration until hits 1 or 89, then compute last to figure which it was


(defn step
  [x]
  (let [digits (->> x
                    str
                    (map #(Character/digit % 10)))]

    (->> digits
         (map #(* % %))
         (reduce +))))

(defn find-terminal
  [x]
  (->> (iterate step x)
       (drop-while #(and (not= % 89)
                         (not= % 1)))
       first))

(defn solve
  []
  (->> (range 1 10000000)
       (map find-terminal)
       (filter (partial = 89))
       count))
