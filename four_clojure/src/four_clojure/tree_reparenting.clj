(ns four-clojure.tree-reparenting)

(defn get-parent
  [tree node]
  (->> tree
       (filter #(some #{node} (val %)))
       (map key)
       first))

(defn get-branch
  [tree node]
  (->> node
       (iterate (partial get-parent tree))
       (take-while some?)))

(defn reparent-child-parent-pair
  ; NOTE: first item (head) is 'rightmost' in the rendered tree!
  [tree [child parent]]
  (-> tree
      (update child #(cons parent %))
      (update parent (fn [children]
                       (remove #(= % child) children)))))

(defn reparent-tree
  [tree new-root]
  (->> (get-branch tree new-root)
       (partition 2 1)
       (reduce reparent-child-parent-pair tree)))

(defn tree-to-list
  [tree root]
  :default)

(defn list-to-tree
  [lst]
  :default)

(defn run
  [new-root lst]
  (-> lst
      list-to-tree
      (reparent-tree new-root)
      tree-to-list))
