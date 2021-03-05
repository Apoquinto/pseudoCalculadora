from src.Stack import Stack

class PseudoCalculadora:
    # Constructor de la clase.
    def __init__(self):
        self._operators = Stack()
        self._result = 0
        self._expression = ''
        self._operands = Stack()
        self._postExpression = ''

    # Comprueba si la operación es posible, en caso de serlo, devuelve la notación postfija.
    def analex(self):
        num = ''
        for token in self._expression:
            # Captura los digitos de un número.
            if token.isdigit():
                num += token
            # Busca los operadores que separan los números.
            elif token in ['+', '-', '/', '*']:
                self._operands.push(num)
                num = ''
                self.evaluate()
                self._operators.push(token)
            # Esto es trampa XD
            elif token == '\n':
                self._operands.push(num)
                num = ''
                self.evaluate()
            else:
                print("Error, elemento no válido en las instrucciones.")

        print(self._operands.getStack())
        print(self._postExpression)
        self.clear()

    def evaluate(self):
        if self._operands.size() == 2 and not self._operators.isEmpty():
            a = self._operands.pop()
            b = self._operands.pop()
            operator = self._operators.pop()
            self._postExpression += 'Oper - ' + str(b) + ' ' + str(a) + ' ' + str(operator) + '\n'
            self._operands.push(eval("{0}{1}{2}".format(b, operator, a)))

    def clear(self):
        self.__init__()

    # Zona de setters y getters.    
    def setExpression(self, expression):
        self._expression = expression.replace(' ', '') + '\n'

    def getExpression(self):
        return self._expression

    def setResult(self, value):
        self._result = value
    
    def getResult(self):
        return self._result
