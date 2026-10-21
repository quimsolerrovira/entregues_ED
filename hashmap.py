class MyHashMap:
    """Taula de hash obert (encadenament separat) amb redimensionament.

    Cada posició de self._table és None o un bucket: una llista de
    parelles [clau, valor] que hi col·lisionen.
    """

    def __init__(self, cap=13):
        self._table = cap * [None]   # m posicions, inicialment buides
        self._n = 0                  # nombre de claus desades

    def _hash_function(self, key):
        return key % len(self._table)          # h(x) = x % m

    def put(self, key: int, value: int) -> None:
        j = self._hash_function(key)
        if self._table[j] is None:             # posició lliure: bucket nou
            self._table[j] = []
        for pair in self._table[j]:
            if pair[0] == key:                 # mateixa clau: actualitzem
                pair[1] = value
                return
        self._table[j].append([key, value])    # clau nova (o col·lisió)
        self._n += 1
        if self._n > len(self._table) // 2:
            self._resize(2 * len(self._table) - 1)

    def get(self, key: int) -> int:
        j = self._hash_function(key)
        if self._table[j] is not None:
            for pair in self._table[j]:
                if pair[0] == key:
                    return pair[1]
        return -1

    def remove(self, key: int) -> None:
        j = self._hash_function(key)
        if self._table[j] is not None:
            for i in range(len(self._table[j])):
                if self._table[j][i][0] == key:
                    self._table[j].pop(i)
                    self._n -= 1
                    if len(self._table[j]) == 0:
                        self._table[j] = None
                    return

    def _resize(self, c):
        old = self._table
        self._table = c * [None]
        self._n = 0
        for bucket in old:
            if bucket is not None:
                for key, value in bucket:
                    self.put(key, value)       # rehashing amb la mida nova

    def __len__(self):
        return self._n