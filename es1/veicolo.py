class Veicolo:
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello

    def scheda(self):
        return f"Marca: {self.marca}, Modello: {self.modello}"