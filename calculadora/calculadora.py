import datetime
import os
import getpass

USER_NAME = "leocarv1"
USER_SENHA = "123"

def soma(x, y):
    print(x+y) 

def subtracao(x, y):
    print(x-y) 

def multiplicacao(x, y):
    print(x*y) 

def divisao(x, y):
    try:
        print(x/y)
    except:
        print("Erro")

def save(txt):
    txtArquivo = open("calculadora/historico.txt", "a", -1, "utf-8")
    txtArquivo.write(txt)
    txtArquivo.close()

def lerArquivo():
    user = str(input("Informe o usuário: "))
    senha = getpass.getpass('Senha: ')   

    user_name = USER_NAME
    user_senha = USER_SENHA

    if user == user_name and senha == user_senha:
        f = open("historico.txt", "r", -1, "utf-8")
        print(f.read())
    else:
        print("Acesso negado!")

def apagarArquivo():
    user = str(input("Informe o usuário: "))
    senha = input('Senha: ')    

    user_name = USER_NAME
    user_senha = USER_SENHA

    if user == user_name and senha == user_senha:
        os.remove("historico.txt")
        print('Arquivo deletado com sucesso!')
    else:
        print("Acesso negado!")

def calculadora():
    menu = """
    Menu:
    A - Soma
    B - Subtração
    C - Multiplicação
    D - Divisão
    E - Ler Histórico
    F - Apagar Histórico
    """
    print(menu)

    opc = input("Escolha uma operação: ").upper()
    
    match opc:
        case ("A"):
            num1 = eval(input("Primeiro número: "))
            num2 = eval(input("Segundo número: "))
            soma(num1, num2)
            txt = f"""
            ========
            Operação: Soma
            Histórico: {num1} + {num2} = {num1+num2}"
            Data: {datetime.datetime.now()}
            ========
            """
            save(txt)

        case ("B"):
            num1 = eval(input("Primeiro número: "))
            num2 = eval(input("Segundo número: "))
            subtracao(num1, num2)

            txt = f"""
            ========
            Operação: Subtração
            Histórico: {num1} - {num2} = {num1-num2}
            Data: {datetime.datetime.now()}
            ========
            """

            save(txt)

        case ("C"):
            num1 = eval(input("Primeiro número: "))
            num2 = eval(input("Segundo número: "))
            multiplicacao(num1, num2)

            txt = f"""
            ========
            Operação: Multiplicação
            Histórico: {num1} * {num2} = {num1*num2}
            Data: {datetime.datetime.now()}
            ========
            """
            
            save(txt)

        case ("D"):
            num1 = eval(input("Primeiro número: "))
            num2 = eval(input("Segundo número: "))
            divisao(num1, num2)

            txt = f"""
            ========
            Operação: divisão
            Histórico: {num1} / {num2} = {num1/num2}
            Data: {datetime.datetime.now()}
            ========
            """

            save(txt)

        case ("E"):
            lerArquivo()

        case ("F"):
            apagarArquivo()

        case _:
            print('Operação inválida!')
            print(menu)