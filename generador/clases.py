import enum


class Material(enum.Enum):
    MULTIMATERIAL = 1
    MACIZO = 2
    HUECO = 3
    INOX = 4
    MADERA = 5
    METAL = 6
    BOLSAFUELLE = 7


class Expositor:
    def __init__(self, blisters, alto, ancho, ganchosF, ganchosC):
        self.blisters = blisters
        self.alto = alto
        self.ancho = ancho
        self.ganchosF = ganchosF
        self.ganchosC = ganchosC

    def toString(self):
        print(
            "Alto = " + self.alto + ", ancho = " + self.ancho + ", ganchos por fila = " + self.ganchosF +
            ", gancho por columna = " + self.ganchosC)


class Blister:
    def __init__(self, material, referencia, largo, ancho):
        self.material = material
        self.referencia = referencia
        self.largo = largo
        self.ancho = ancho

    def toString(self):
        print(
            "Material = " + self.material + ", referencia = " + self.referencia + ", tamaño = " + self.largo + " X " + self.ancho)
