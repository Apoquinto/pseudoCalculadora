from src.OuterCLI import *

def main():
    # Inicializo la CLI
    outerCLI = OuterCLI()

    while outerCLI.On:
        outerCLI.input_handler()

if __name__ == "__main__":
    main()