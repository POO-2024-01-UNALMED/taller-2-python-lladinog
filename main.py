class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        colores_permitidos = ["rojo", "verde", "amarillo", "negro", "blanco"]
        if color.lower() in colores_permitidos:
            self.color = color
        else:
            print("Color no permitido.")

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro):
        self.registro = registro

    def asignarTipo(self, tipo):
        if tipo.lower() in ["electrico", "gasolina"]:
            self.tipo = tipo
        else:
            print("Tipo no permitido.")

class Auto:
    cantidadCreados = 0

    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        Auto.cantidadCreados += 1

    def cantidadAsientos(self):
        return sum(1 for asiento in self.asientos if isinstance(asiento, Asiento))

    def verificarIntegridad(self):
        registros = {self.registro, self.motor.registro}
        registros.update(asiento.registro for asiento in self.asientos if isinstance(asiento, Asiento))
        
        if len(registros) == 1:
            return "Auto original"
        else:
            return "Las piezas no son originales"

