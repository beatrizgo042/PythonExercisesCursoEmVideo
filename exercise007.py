#Desenvolva um programa que leia duas notas de um aluno, calcule e mostre a sua média.

nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))

media = (nota1 + nota2) / 2

print(f"A média entre {nota1} e {nota2} é igual a {media:.1f}.")