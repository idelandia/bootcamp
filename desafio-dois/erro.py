def calcular_media(valores):
    tamanho = 0
    soma = 0.0
    for i, valor in valores:
        soma += valor
        tamanho += 1
    media = soma / tamanho
    return media

continuar = True
valores = []
while continuar:
    valor = input('Digite um número para entrar na sua média ou "ok" para calcular o valor: ')
    if valor.lower() == 'ok':
        continuar = False
    else:
        valores.append(float[valor])

media = calcular_media(valores)
print('A média para os valores calculados de {} foi de {}'.format(valores, media))