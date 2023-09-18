# 1
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
if (numero1 > numero2):
    maior = numero1
else:
    maior: numero2

print(f"O maior número foi: {maior}")


# 2
turno = input("Em qual turno você estuda? (M - Matutino, V - Vespertino, N - Noturno): ")
if turno == 'M':
    print("Bom Dia!")
elif turno == 'V':
    print("Boa Tarde!")
elif turno == 'N':
    print("Boa Noite!")
else:
    print("Valor Inválido! Por favor, digite M, V ou N.")


#3
while True:
    nota = float(input("Digite uma nota entre 0 e 10: "))
    if 0 <= nota <= 10:
        print("Nota válida:", nota)
        break 
    else:
        print("Valor inválido! Por favor, digite uma nota entre 0 e 10.")
