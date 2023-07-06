menu = """
    A - Criar Arquivo
    B - Ler arquivo
    C - Editar Arquivo
    X - Menu Principal
"""
    
def criarArquivo(nome):
    try:
        arq = open(nome, "x")
        print("Arquivo criado com sucesso!")
    except:
        print("Erro ao criar novo arquivo!")

def lerArquivo(arquivo):
    f = open(arquivo, "r", -1, "utf-8")
    for x in f:
        print(x)

def editarArquivo(arquivo, txt):
    arquivo = open(arquivo, "a", -1, "utf-8")
    arquivo.write(txt)
    arquivo.close()

def start():
    print(menu)
    opcInicio = input('Escolha uma opção: ').upper()

    match opcInicio:
        case ("A"):
            nome = input("Informe o nome do arquivo: ")
            criarArquivo(nome)

        case ("B"):
            nome = input("Informe o nome do arquivo: ")
            lerArquivo(nome)

        case ("C"):
            nome = input("Informe o nome do arquivo: ")
            txt = input("Informe o texto que deve ser inserido: \n")

            editarArquivo(nome, txt + "\n")

        case ("X"):
            print("Saindo...")

        case _:
            print("Opção inválida!")


