(ns four-clojure.game-of-life)

; board is a map from (row,col) -> bool (alive?)

(defn char-to-alive? [c] (= c \#))

(defn size
  [board]
  (let [[max-row max-col] (-> board keys sort last)]
    ; b/c zero-indexing
    [(inc max-row) (inc max-col)]))

(defn row-str-to-board
  [row-str row-num]
  (->> (seq row-str)
       (map char-to-alive?)
       (map vector (range))
       (map (fn [[col-num alive?]]
              [[row-num col-num] alive?]))
       (into {})))

(defn row-strs-to-board
  [row-strs]
  (reduce
   (fn [board [row-str row-num]]
     (into board (row-str-to-board row-str row-num)))
   {}
   (map vector row-strs (range))))

(defn alive?-to-char [a]
  (if a
    \#
    \space))

(defn build-row-str
  [board num-cols row-num]
  (->> (range num-cols)
       (map #(get board [row-num %]))
       (map alive?-to-char)
       (apply str)))

(defn board-to-row-strs
  [board]
  (let [[num-rows num-cols] (size board)]
    (->> (range num-rows)
         (map #(build-row-str board num-cols %))
         vec)))

(defn next-val
  [row col board]
  (let [num-live-neighbors (->> (for [r [(dec row) row (inc row)]
                                      c [(dec col) col (inc col)]]
                                  [r c])

                                (filter #(not= [row col] %))
                                (filter #(get board %))
                                count)
        alive? (get board [row col])]

    (cond
      (and alive? (< num-live-neighbors 2)) false

      (and alive? (<= num-live-neighbors 3)) true

      (and alive? (> num-live-neighbors 3)) false ; overpopulation

      (and (not alive?) (= num-live-neighbors 3)) true ; reproduction

      :else false)))

(defn next-board
  [board]
  ; generate board for next time step
  (let [[num-rows num-cols] (size board)]
    (->> (for [row (range num-rows)
               col (range num-cols)]

           [[row col]
            (next-val row col board)])

         (into {}))))

(defn game-of-life
  "Problem 94.

  Return the next game of life iteration."
  [row-strs]
  (-> row-strs
      row-strs-to-board
      next-board
      board-to-row-strs))
