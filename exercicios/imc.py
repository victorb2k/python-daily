# Objetivo: receber altura e peso do usuário e calcular o IMC
# Classificar: abaixo do peso / normal / sobrepeso / obesidade

# Fórmula: IMC = peso / (altura * altura)

altura = float(input("Informe sua altura em metros (ex: 1.80): "))
peso = float(input("Informe seu peso em kg: "))

imc = peso / (altura * altura)

if imc < 22:
    print(f"IMC = {imc:.2f}")
    print("Baixo Peso")
elif imc < 27:
    print(f"IMC = {imc:.2f}")
    print("Normal")
elif imc < 29:
    print(f"IMC = {imc:.2f}")
    print("Sobrepeso")
else:
    print(f"IMC = {imc:.2f}")
    print("Obesidade")
    