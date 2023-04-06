
# Exercício de Calcular média 
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
media = (nota1 + nota2) / 2
if media > 6 or media == 6:
    print("Parabéns! você passou com média: ", media)
else : 
    print("Você foi reprovado com a média: ", media)
    

#Exercício de soma de numeros apenas pares 

num1 = int(input("Primeiro numero: "))
num2 = int(input("Segundo numero: "))
num3 = int(input("Terceiro numero: "))
num4 = int(input("Quarto numero: "))
soma_pares = 0 
if num1 % 2 == 0:
    soma_pares += num1
if num2 % 2 == 0:
    soma_pares += num2
if num3 % 2 == 0:
    soma_pares += num3
if num4 % 2 == 0:
    soma_pares += num4
print("A soma dos numeros pares é:", soma_pares)

#Exercício de soma dos dois maiores numeros ( considerando que todos os 3 numeros são diferentes)

num1 = int(input("Escreva o primeiro numero: "))
num2 = int(input("Escreva o segundo numero: "))
num3 = int(input("Escreva o terceiro numero: "))

if num1 > num2 and num1 > num3:
    if num2 > num3: 
        print("A soma dos dois maiores numeros é: ", num1 + num2)
    else:
        print("A soma dos dois maiores numeros é: ", num1 + num3)
elif num2 > num1 and num2 > num3:
    if num1 > num3: 
        print("A soma dos dois maiores numeros é: ", num2 + num1)
    else:
        print("A soma dos dois maiores numeros é: ", num2 + num3)
elif num1 > num2:
    print("A soma dos dois maires numeros é: ", num3 + num1)
else: print("A soma dos dois maiores numeros é :", num3 + num2)

