# servicios/garaje_servicio.py
from modelos.vehiculo import Vehiculo

class GarajeServicio:
    def __init__(self):
        self._vehiculos = []

    def agregar_vehiculo(self, vehiculo: Vehiculo):
        # Validaciones simples
        if not vehiculo.placa or not vehiculo.marca or not vehiculo.propietario:
            raise ValueError("Todos los campos son obligatorios.")
        # Evitar placas duplicadas (opcional, pero útil)
        if any(v.placa.lower() == vehiculo.placa.lower() for v in self._vehiculos):
            raise ValueError("La placa ya está registrada.")
        self._vehiculos.append(vehiculo)

    def listar_vehiculos(self):
        # Devolvemos una copia para evitar modificaciones externas
        return list(self._vehiculos)

    def limpiar_registros(self):
        self._vehiculos.clear()