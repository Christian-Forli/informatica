from veicolo import Veicolo

class Moto(Veicolo):
    def __init__(self, marca, modello, cilindrata):
        super().__init__(marca, modello)
        self.cilindrata = cilindrata

    def scheda(self):
        return f"{super().scheda()}, Cilindrata: {self.cilindrata}cc"