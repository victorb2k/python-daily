a, b, c = map(float, input().split())
pi = 3.14159

#a) a área do triângulo retângulo que tem A por base e C por altura.
area_triangulo = ( a * c ) / 2
#b) a área do círculo de raio C. (pi = 3.14159)
area_circulo = pi * c**2
#c) a área do trapézio que tem A e B por bases e C por altura.
area_trapezio = ((a + b) * c) / 2
#d) a área do quadrado que tem lado B.
area_quadrado = b ** 2
#e) a área do retângulo que tem lados A e B.
area_retangulo = a * b

print(f"TRIANGULO: {area_triangulo:.3f}")
print(f"CIRCULO: {area_circulo:.3f}")
print(f"TRAPEZIO: {area_trapezio:.3f}")
print(f"QUADRADO: {area_quadrado:.3f}")
print(f"RETANGULO: {area_retangulo:.3f}")