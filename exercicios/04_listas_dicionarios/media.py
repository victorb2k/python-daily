"""
Objetivo: Calcular a média de notas de um aluno usando listas.
Nível: Iniciante
"""

notas = [float(input(f"Digite a nota {i+1}: ")) for i in range(3)]
media = sum(notas) / len(notas)

print(f"Média: {media:.2f}")
