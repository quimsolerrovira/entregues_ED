class MinStack:
    """Pila que permet obtenir el mínim en O(1).

    Cada posició guarda una parella (valor, mínim fins aquí).
    Així, el mínim actual sempre és el segon element del cim.
    """

    def __init__(self):
        # Llista pròpia de cada instància: dues piles no comparteixen dades.
        self.stack = []

    def push(self, val: int) -> None:
        if self.stack:
            current_min = self.stack[-1][1]
            new_min = val if val < current_min else current_min
        else:
            new_min = val
        self.stack.append((val, new_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


if __name__ == "__main__":
    s = MinStack()
    s.push(-2)
    s.push(0)
    s.push(-3)
    print(s.getMin())  
    s.pop()
    print(s.top())     
    print(s.getMin())  

