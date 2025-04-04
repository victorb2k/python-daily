"""
Objetivo: Verificar qual valor é maior entre dois números informados.
Nível: Iniciante
"""
a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))

if a > b:
    print(f"{a} é maior que {b}")
elif b > a:
    print(f"{b} é maior que {a}")
else:
    print("Os números são iguais.")

"""
Objetivo: Verificar qual valor é menor entre dois números informados.
Nível: Iniciante
"""
a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))

if a < b:
    print(f"{a} é menor que {b}")
elif b > a:
    print(f"{b} é menor que {a}")
else:
    print("Os números são iguais.")