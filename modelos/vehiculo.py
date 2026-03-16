# modelos/vehiculo.py
class Vehiculo:
    def __init__(self, placa: str, marca: str, propietario: str):
        self.placa = placa.strip()
        self.marca = marca.strip()
        self.propietario = propietario.strip()

    def to_tuple(self):
        return (self.placa, self.marca, self.propietario)