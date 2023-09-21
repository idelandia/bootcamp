class Carro:
    def __init__(self, cor, modelo):
        self.ligado = False
        self.cor = cor
        self.modelo = modelo
        self.velocidade = 0.0
        self.limite_velocidade = 100.0

    def liga(self):
       self.ligado = True
           
    def desliga(self):
        self.ligado = False
        self.velocidade = 0.0
           
    def acelera(self):
        if self.ligado == False:
            return
        
        if self.velocidade < self.limite_velocidade:
            self.velocidade += 5

    def desacelera(self):
        if self.ligado == False:
            return
        
        if self.velocidade >0:
            self.velocidade -= 5 

    def __str__(self):
        ligado_str = "ligado" if self.ligado == True else "desligado"
        return f"Carro {self.modelo} da cor {self.cor} está {ligado_str}, à velocidade de {self.velocidade} km/h."

    

# Criando uma instância da classe Carro
carro = Carro("preto", "sedan")
print(carro)

# Ligando o carro
carro.liga()
print(carro)

# Acelerando o carro
carro.acelera()
print(carro)

for _ in range(5):
    carro.acelera()

print(carro)

# Desacelerando o carro
carro.desacelera()
print(carro)

for _ in range(3):
    carro.desacelera()
print(carro)

# Desligando o carro
carro.desliga()
print(carro)
