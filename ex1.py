class carro:
    def __init__(self, marca, modelo, ano, motor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.motor = motor
    
uno = carro("Fiat", "Uno", 2010, 1.0)
gol = carro("Volkswagem", "Gol", 2012, 2.0)

print(uno.motor)
print(gol.motor)