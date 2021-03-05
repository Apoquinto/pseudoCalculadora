from src.Stack import Stack

class PseudoCalculadora:
    # Constructor de la clase.
    def __init__(self):
        self._operators = Stack()
        self._result = 0
        self._expression = ''
        self._postExpression = Stack()

    # Comprueba si la operación es posible, en caso de serlo, devuelve la notación postfija.
    def analex(self):
        num = ''
        for token in self._expression:
            if token.isdigit():
                num += token
            # Busca los operadores que separan los n[umeros]
            elif token in ['+', '-', '/', '*']:
                self._operators.push(token)
                self._postExpression.push(num)
                num = ''
            # Esto es trampa XD
            elif token == '!':
                self._postExpression.push(num)
                num = ''
            else:
                return False

        print(self._postExpression.getStack())

    def clear(self):
        self._expression = ''
        self._result = 0

    # Zona de setters y getters.    
    def setExpression(self, expression):
        self._expression = expression.replace(' ', '') + '!'

    def getExpression(self):
        return self._expression

    def setResult(self, value):
        self._result = value
    
    def getResult(self):
        return self._result