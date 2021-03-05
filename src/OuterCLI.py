from src.PseudoCalculadora import PseudoCalculadora

class OuterCLI:
    # Propiedades inmutables para la CLI.
    OK = '\033[92m'         # GREEN
    WARNING = '\033[93m'    # YELLOW
    FAIL = '\033[91m'       # RED
    RESET = '\033[0m'       # RESET COLOR
    
    # Inicializacion del objeto
    def __init__(self):
        self.On = True
        self._calculadora = PseudoCalculadora() 
    
    def init_msg(self):
        print(self.msg_green("[OuterCal]~"), end = ' ')

    # Return a string in GREEN
    def msg_green(self, msg):
        return self.OK + msg + self.RESET

    # Return a string in Yellow
    def msg_yellow(self, msg):
        return self.WARNING + msg + self.RESET

    # Return a string in RED
    def msg_red(self, msg):
        return self.FAIL + msg + self.RESET

    # Espera la entrada de los comandos
    def input_handler(self):
        self.init_msg()
        # Get command
        command = input()
        command = command.split()
        # Commands definition
        if(len(command) < 1):
            pass
        elif(command[0] == '\h'):
            print(self.msg_green("Bienvenido al sistema de ayuda de esta CLI :D"))
            print(self.msg_green("\q") + "Salir de la CLI." )
        elif(command[0] == '\q'):
            self.On = False
        else:
            self._calculadora.setExpression(command[0])
            self._calculadora.analex()
