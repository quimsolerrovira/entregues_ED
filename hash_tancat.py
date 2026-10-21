# Estats d'una posició de la taula (hash tancat). NO canvieu aquests valors.
LLIURE = "L"
OCUPAT = "O"
ESBORRAT = "B"


class MyHashMap:
    """Taula de hash tancat (adreçament obert) amb sondeig lineal.

    Cada posició de self._table és una llista [clau, valor, estat].
    """

    def __init__(self, cap=13):
        # Cada posició ha de ser una llista diferent (no fer cap * [[...]])
        self._table = [[None, None, LLIURE] for _ in range(cap)]
        self._n = 0

    def _hash_function(self, key):
        return key % len(self._table)          # h(x) = x % M

    def _find(self, key):
        """Retorna la posició on és la clau, o None si no hi és."""
        M = len(self._table)
        h = self._hash_function(key)
        for i in range(M):
            j = (h + i) % M
            if self._table[j][2] == LLIURE:     # la clau no hi és
                return None
            if self._table[j][2] == OCUPAT and self._table[j][0] == key:
                return j
        return None

    def put(self, key: int, value: int) -> None:
        M = len(self._table)
        h = self._hash_function(key)
        lloc = None                            # primera ESBORRAT/LLIURE trobada
        for i in range(M):
            j = (h + i) % M
            if self._table[j][2] == OCUPAT:
                if self._table[j][0] == key:   # mateixa clau: actualitzem
                    self._table[j][1] = value
                    return
            else:
                if lloc is None:
                    lloc = j
                if self._table[j][2] == LLIURE:  # la clau no pot ser més enllà
                    break
        self._table[lloc] = [key, value, OCUPAT]
        self._n += 1
        if self._n > len(self._table) // 2:
            self._resize(2 * len(self._table) - 1)

    def get(self, key: int) -> int:
        j = self._find(key)
        if j is None:
            return -1
        return self._table[j][1]

    def remove(self, key: int) -> None:
        j = self._find(key)
        if j is not None:
            self._table[j] = [None, None, ESBORRAT]
            self._n -= 1

    def _resize(self, c):
        old = self._table
        self._table = [[None, None, LLIURE] for _ in range(c)]
        self._n = 0
        for pos in old:
            if pos[2] == OCUPAT:               # les ESBORRAT desapareixen
                self.put(pos[0], pos[1])

    def __len__(self):
        return self._n
