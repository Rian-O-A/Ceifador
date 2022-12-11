
from time import sleep

class carro:
    def __init__(self, marca, modelo, cor, ano, estado) -> None:
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.estado = estado

    def Ligar(self):
        print(f"Ligando carro {self.modelo}!")

    def Desligar(self):
        print(f"Desligando carro {self.modelo}!")

    def Informar(self):
        print(f"Marca:{self.marca}\nModelo: {self.modelo}\nAno: {self.ano}\nCor: {self.cor}\nEstado: {self.estado}")

    def explodir(self):
        print("Seu carro explodira em 10 segundos")
        for temp in range(10, 0, -1):
            print(temp)
            sleep(1)

carros1 = carro(marca='Chevrolet', modelo='Onix', cor='Branca', ano='2020', estado='Perfeito')   
carros1.Ligar()
carros1.Desligar()
carros1.Informar()
carros1.explodir()