#1
def converter():
    valor = input("Digite o valor em reais: ")
    moedas = {
        "Dólar Americano": 4.91,
        "Peso Argentino": 0.02,
        "Dólar Australiano": 3.18,
        "Dólar Canadense": 3.64,
        "Franco Suíço": 0.42,
        "Euro": 5.36,
        "Libra Esterlina": 6.21
    }

    for moeda, valor_moeda in moedas.items():
        print(f"{moeda}: {float(valor)/valor_moeda}")

#2
km = float(input("Digite a quantidade de quilômetros percorridos: "))
dias = float(input("Digite a quantidade de dias de aluguel: "))

valor_dia = 80
valor_km = 0.20

print(f"O preço a pagar é:{(valor_km * km) + (valor_dia * dias)}")

#3
salario = float(input("Digite o salário do funcionário: "))
if salario <= 1000:
       print(f"O novo salário é R${salario*1.2}")
elif salario <= 2800:
       print(f"O novo salário é R${salario*1.1}")
else:
        print(f"O novo salário é R${salario*1.05}")


#4
def leiaInt():
    while True:
        try:
            valor = int(input("Digite um número inteiro: "))
        except ValueError:
            print("Por favor, digite um valor inteiro válido.")


numero = leiaInt()
print(f"Você digitou: {numero}")


