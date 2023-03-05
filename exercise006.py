import math

#Crie um algoritmo que leia um número e mostre seu dobro, triplo e raiz quadrada.

n = int(input("Digite um número: "))

d = n * 2
t = n * 3
r = math.sqrt(n)

print(f"O dobro de {n} é {d}")
print(f"O triplo de {n} é {t}")
print(f"E a raíz quadrada de {n} é {r:.2f}")