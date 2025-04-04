"""
Objetivo: Criar uma calculadora simples usando funções.
Nível: Iniciante
"""

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b if b != 0 else "Erro: divisão por zero"

print("Calculadora")
x = float(input("Digite o primeiro número: "))
y = float(input("Digite o segundo número: "))
op = input("Escolha a operação (+ - * /): ")

if op == '+':
    print("Resultado:", somar(x, y))
elif op == '-':
    print("Resultado:", subtrair(x, y))
elif op == '*':
    print("Resultado:", multiplicar(x, y))
elif op == '/':
    print("Resultado:", dividir(x, y))
else:
    print("Operação inválida")
