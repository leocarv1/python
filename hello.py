from classe import Teste

p = Teste("Leo", 26)
print(p.name)
print(p.age)

def sayHello():
	print('Hello World!')
def soma(a, b):
	print(a+b)

def sayMyName(name):
	print('Olá, ' + name)

sayHello()
x = eval(input('primeiro: '))
y = eval(input('segundo: '))
soma(x, y)
nome = input('nome: ')
sayMyName(nome)
