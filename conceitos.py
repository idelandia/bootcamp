# 1 
numero = float(input("Digite um número: "))
print(f"O número informado foi {numero}")

# 2 
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
soma = numero1 + numero2
print(f"A soma dos números é: {soma}")

# 3
celsius = float(input("Digite a temperatura em graus Celsius: "))
fahrenheit = (celsius * 9/5) + 32 #fahrenheit = celsius * (9/5) + 32
print(f"A temperatura em graus Fahrenheit é: {fahrenheit}")

# 4
valor_hora = float(input("Digite o valor que você ganha por hora: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))
salario_mensal = valor_hora * horas_trabalhadas
print(f"Seu salário no referido mês é: R${salario_mensal:.2f}")

