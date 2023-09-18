#1
def programando (num1, num2, num3):
    soma = num1 +num2 +num3
    print(soma)

programando(1, 2, 3)

#2
def reverte(numero):
    numero_str = str(numero)
    reverso = []

    for n in range(len(numero_str)-1, -1, -1):
        reverso.append(numero_str[n])

    reverso = int(''.join(reverso))
    return reverso

num = int(input("Digite um número: "))
print(
    reverte(num)
)

#3
def celsius_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def menu():
    print("Escolha uma opção:")
    print("1 - Converter de Celsius para Fahrenheit")
    print("2 - Converter de Fahrenheit para Celsius")
    opcao = input("Digite o número da opção desejada: ")
    return opcao

opcao = menu()

if opcao == '1':
        celsius = float(input("Digite a temperatura em graus Celsius: "))
        resultado = celsius_fahrenheit(celsius)
        print(f"{celsius}°C equivalem a {resultado}°F")

elif opcao == '2':
        fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
        resultado = fahrenheit_celsius(fahrenheit)
        print(f"{fahrenheit}°F equivalem a {resultado}°C")

else:
        print("Opção inválida. Por favor, escolha 1 ou 2.")


