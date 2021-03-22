print('====================================')
print('1. Adição\n2. Subtração\n3. Multiplicação\n4. Divisão')
print('====================================')
print('Escolha a operação: (1\\2\\3\\4):')
op = input()

def entrada ():
    global x
    global y
    print('Digite o primeiro numero: ')
    x = int(input())
    print('Digite o segundo numero: ')
    y = int(input())
    return(x,y)
def addition (x,y):
    result = x + y
    print(x, '+', y, '=', result)
def subtraction (x,y):
    result = x - y
    print(x, '-', y, '=', result)
def multiplication (x,y):
    result = x * y
    print(x, 'x', y, '=', result)
def division(x,y):
    result = x / y
    print(x, '/', y, '=', result)

if op == '1':
    entrada()
    addition(x,y)
elif op == '2':
    entrada()
    subtraction(x,y)
elif op == '3':
    entrada()
    multiplication(x,y)
elif op == '4':
    entrada()
    division(x,y)
else:
    print('Operação Invalida.')