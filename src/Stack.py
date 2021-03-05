class Stack:
    # constructor de la pila.
    def __init__(self):
        self._elements = []

    # Devuelve un booleano que representa si contiene elementos la pila.
    def isEmpty(self):
        return self._elements == []

    # Agrega un elemento a la pila.
    def push(self, x):
        self._elements.append(x)

    # Devuelve el último elemento de la pila y lo desapila.
    def pop(self):
        if self.isEmpty():
            raise ValueError("Stack empty")
        else:
            return self._elements.pop()

    # Devuelve el tamaño de la pila.
    def size(self):
        return len(self._elements)

    # Devuelve los elementos de la pila
    def getStack(self):
        return self._elements