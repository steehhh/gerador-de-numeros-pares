print("vamos ver quais os primeiros numeros pares do numero de sua escolha!")
tamanhoS = int(input("\ndigite algum numero para verificar:"))
print("\n\nvoce escolheu o numero ",tamanhoS,"!")

print("\n\nos primeiros numeros pares ate seu numero inserido sao: \n\n")

contador = 1

while contador <= tamanhoS:
    if contador % 2 == 0: 
        print(contador, end=(" - "))
    contador += 1 
else:
    contador += 1
