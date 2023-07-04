from calculadora import calculadora



def criarArquivo(nome):
    try:
        arq = open(nome, "x")
    except:
        print("Erro ao criar novo arquivo!")

def lerArquivo(arquivo):
    f = open(arquivo, "r", -1, "utf-8")
    print(f.read())

def editarArquivo(arquivo, txt):
    arquivo = open(arquivo, "a", -1, "utf-8")
    arquivo.write(txt)
    arquivo.close()

while True:
    menuInicio = """
    Menu:
    A - Calculadora
    B - Criar Arquivo
    C - Ler arquivo
    D - Editar Arquivo
    X - Sair
    """
    print(menuInicio)
    opcInicio = input('Escolha uma opção: ').upper()

    match opcInicio:
        case ("A"):
            calculadora()

        case ("B"):
            nome = input("Informe o nome do arquivo: ")
            criarArquivo(nome)
            print("Arquivo criado com sucesso!")

        case ("C"):
            nome = input("Informe o nome do arquivo: ")
            lerArquivo(nome)

        case ("D"):
            nome = input("Informe o nome do arquivo: ")
            txt = input("Informe o texto que deve ser inserido: \n")

            editarArquivo(nome, txt)

        case ("X"):
            print("Saindo...")
            break

        case _:
            print("Opção inválida!")