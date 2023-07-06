from calculadora.calculadora import calculadora
import mouse
from arquivo import arquivo

while True:
    menuInicio = """
    Menu:
    A - Calculadora
    B - Arquivo
    E - Desenhar um espiral no Paint
    X - Sair
    """
    print(menuInicio)
    opcInicio = input('Escolha uma opção: ').upper()

    match opcInicio:
        case ("A"):
            calculadora()

        case ("B"):
            arquivo.start()

        case ("E"):
            mouse.draw()

        case ("X"):
            print("Saindo...")
            break

        case _:
            print("Opção inválida!")