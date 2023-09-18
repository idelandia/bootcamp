#1
listaMedias = []
listaNotas = []

qtdAlunos = 10
qtdNotas = 10

for aluno in range(qtdAlunos):
   listaNotas.append ({})
for nota in range(qtdNotas):
    listaNotas[aluno].append(
        float(
            input(f"Digite a nota {nota+1} do aluno {aluno+1}")
        )
    )
for notas in listaNotas:
    listaMedias.append(
        sum(notas) / len(notas)
    )

alunos_aprovados = sum(1 for media in listaMedias if media >= 7.0)
print(f"Número de alunos com média maior ou igual a 7.0: {alunos_aprovados}")
     
#2
nome = input("Digite seu nome: ")
nome_invertido = []
for i in range(len(nome) -1, -1, -1):
    nome_invertido.append(nome[i].upper())

print(''.join(nome_invertido))

#3
dicionario = {"banana": 'fruta', "casa": 'imovel', "laranja": 'fruta'}
print(dicionario)
valores_emitidos = all(valor for valor in dicionario.values())

if valores_emitidos:
    print("True")
else: 
    print("False")

#4