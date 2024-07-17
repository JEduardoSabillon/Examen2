import math


class Figura:
    def __init__(self, tipo, radio):
        self.tipo = tipo
        self.radio = radio

    def calcular_area(self):
        if self.tipo.lower() == 'circulo':
            return math.pi * (self.radio ** 2)
        elif self.tipo.lower() == 'esfera':
            return 4 * math.pi * (self.radio ** 2)
        else:
            raise ValueError("Tipo de figura no soportada para el cálculo de área")

    def calcular_volumen(self):
        if self.tipo.lower() == 'esfera':
            return (4 / 3) * math.pi * (self.radio ** 3)
        else:
            raise ValueError("Tipo de figura no soportada para el cálculo de volumen")

    def __str__(self):
        return f'Figura: {self.tipo.capitalize()}, Radio: {self.radio}'


class Reconocimiento:
    def __init__(self):
        self.figuras = []

    def agregar_figura(self, figura):
        self.figuras.append(figura)

    def reconocer_y_calcular(self):
        for figura in self.figuras:
            try:
                area = figura.calcular_area()
                print(f'El área del {figura.tipo} con radio {figura.radio} es: {area:.2f}')
            except ValueError as e:
                print(e)
                try:
                    volumen = figura.calcular_volumen()
                    print(f'El volumen del {figura.tipo} con radio {figura.radio} es: {volumen:.2f}')
                except ValueError as e:
                    print(e)


# Ejemplo de uso
circulo = Figura('circulo', 5)
esfera = Figura('esfera', 5)

reconocimiento = Reconocimiento()
reconocimiento.agregar_figura(circulo)
reconocimiento.agregar_figura(esfera)

reconocimiento.reconocer_y_calcular()

