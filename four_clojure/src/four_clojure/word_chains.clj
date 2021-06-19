(ns four-clojure.word-chains)

; dag-map is of form {word -> #{words}

(defn longest-path-len
  ([dag-map]
   (->> (keys dag-map)
        (map #(longest-path-len dag-map % #{} 0))
        (apply max)))

  ([dag-map from-word seen-words len]
   ; BFS where we keep track of longest length
   (let [new-neighbors (apply disj
                              (get dag-map from-word)
                              seen-words)

         longest-path-lens (map #(longest-path-len dag-map
                                                   %
                                                   (conj seen-words %)
                                                   (inc len))
                                new-neighbors)]
     (if (empty? longest-path-lens)
       len
       (apply max longest-path-lens)))))

(defn edit-distance
  [s1 s2]
  (cond
    (empty? s1) (count s2)

    (empty? s2) (count s1)

    :else (min (+ (if (= (first s1) (first s2))
                    0
                    1)
                  (edit-distance (rest s1) (rest s2)))

               (inc (edit-distance s1 (rest s2)))

               (inc (edit-distance (rest s1) s2)))))

(defn build-dag-map
  [words]
  (let [neighbors (fn [word]
                    (->> words
                         (filter #(= 1 (edit-distance % word)))
                         set))]

    (->> words
         (map (juxt identity neighbors))
         (into {}))))

(defn word-chains
  "Problem 82.

  Returns true iff all words can be arranged in one continuous word chain."
  [words]
  (= (longest-path-len (build-dag-map words))
     (count words)))
