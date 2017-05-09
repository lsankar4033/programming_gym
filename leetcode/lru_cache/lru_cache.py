# Problem here: https://leetcode.com/problems/lru-cache/#/description
# An O(1) implementaiton can be built using a doubly linked list and a dict. The doubly linked list is used
# to keep track of recency and the dict points to specific nodes in the dll.

class LRUCache():
    """LRU cache implemented using a hash map and doubly linked list for O(1) time operations.
    """

    class DLLNode():
        """Node in the recency-tracking doubly linked list.
        """
        def __init__(self, k, v):
            self.prev = None
            self.next = None
            self.k = k
            self.v = v


    def __init__(self, capacity):
        assert capacity > 0, "Must specify a positive capacity!"

        self.capacity = capacity
        self.dll_front = None # Front = most recent
        self.dll_back = None
        self.hm = {}

    def _remove_key_from_dll(self, key):
        if key in self.hm:
            dll_node = self.hm[key]

            # Remove node from current position in dll
            if dll_node.prev is not None:
                dll_node.prev.next = dll_node.next
            else:
                self.dll_front = dll_node.next
            if dll_node.next is not None:
                dll_node.next.prev = dll_node.prev
            else:
                self.dll_back = dll_node.prev

            return dll_node
        else:
            return None

    def _add_node_to_dll_front(self, dll_node):
        dll_node.prev = None
        dll_node.next = self.dll_front

        if self.dll_front is not None:
            self.dll_front.prev = dll_node
        self.dll_front = dll_node

        # If this is the first node, make sure to also add it to the back
        if self.dll_back is None:
            self.dll_back = dll_node

    def _evict_once(self):
        node_to_evict = self.dll_back
        assert node_to_evict is not None, "Attempting to evict with empty cache!"

        if node_to_evict.prev is not None:
            node_to_evict.prev.next = None
        self.dll_back = node_to_evict.prev

        self.hm.pop(node_to_evict.k, None)

    def get(self, key):
        """Returns the value for the provided key if it exists in the cache and -1 otherwise.
        """
        dll_node = self._remove_key_from_dll(key)
        if dll_node is None:
            return -1
        else:
            self._add_node_to_dll_front(dll_node)
            return dll_node.v

    def put(self, key, value):
        """Puts the specified key value pair into the cache and evicts least recently used items if the cache
        has more than self.capacity items.
        """
        self._remove_key_from_dll(key)

        # Put new node in dict and dll
        new_node = LRUCache.DLLNode(key, value)
        self.hm[key] = new_node
        self._add_node_to_dll_front(new_node)

        # Evict down to capacity
        while len(self.hm) > self.capacity:
            self._evict_once()
