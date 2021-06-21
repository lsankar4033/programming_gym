(ns four-clojure.sequence-reductions)

(defn reductions-2
  ([f val coll]
   (lazy-seq
    (if (empty? coll) (list val)
        (cons val
              (reductions-2 f
                            (f val (first coll))
                            (rest coll))))))

  ([f coll] (reductions-2 f (first coll) (rest coll))))
