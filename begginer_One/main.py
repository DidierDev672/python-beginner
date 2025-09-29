def myFunction():
    """ Esta es una funcion simple que se ejecutara... """
    print("!Hola desde mi_funcion");

def main():
    """ La funcion principal que llamara a otras funciones. """
    print("Iniciando el programa...");
    myFunction(); #? Llama a la otra funcion

if __name__ == '__main__':
    main();