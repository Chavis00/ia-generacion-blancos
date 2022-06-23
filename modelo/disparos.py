from random import sample
from itertools import product
from math import sqrt



IMPACTOS_TOT = 6
DISPAROS_SERIE = IMPACTOS_TOT//2

class ValueTooSmall(Exception):
    """ Cuando el alto y ancho de la zona de impactos no llega a contener los impactos totales """
    pass

class Disparo:
    """ Disparo individual que contiene información de posicion y el marcador que lo representa en el blanco """
    def __init__(self, posicion:tuple, indicador:int = 0):
        self.posicion = posicion
        self.indicador = indicador

    def __repr__(self):
        return str(self.posicion) + "->" + str(self.indicador)

class Impactos(list):
    """ Genera y contiene una lista de 6 disparos, como los realizados en el blanco de MOTE """
    def __init__(self, *args):
        list.__init__(self, *args)
        self.max_ancho = 0
        self.max_alto = 0
        self.min_ancho = 0
        self.min_alto = 0

    def generar_disparos(self,min_ancho, max_ancho, min_alto, max_alto):
        self.max_ancho = max_ancho
        self.max_alto = max_alto
        self.min_ancho = min_ancho
        self.min_alto = min_alto
        if max_ancho * max_alto >= IMPACTOS_TOT:
            posiciones = sample(list(product(range(max_ancho), range(max_alto))), k=IMPACTOS_TOT)
            for pos in posiciones[:DISPAROS_SERIE]:
                self.append(Disparo(posicion=pos,indicador=1))

            for pos in posiciones[DISPAROS_SERIE:]:
                self.append(Disparo(posicion=pos, indicador=-1))
            # print(f'Superficies: {superficies}')

        else:
            raise ValueTooSmall

    def generar_dispersos(self, min_ancho, max_ancho,min_alto, max_alto, area_deseada = 12.5):
        """Garantiza que al menos uno de los dos triangulos generados tiene un área superiror a la
        maxima que puede tener un triangulo aprobado"""
        self.max_ancho = max_ancho
        self.max_alto = max_alto
        self.max_ancho = min_ancho
        self.max_alto = min_alto
        area = 0.0

        while area <= area_deseada:

            self.clear()
            self.generar_disparos(min_ancho=min_ancho, max_ancho=max_ancho,min_alto=min_alto, max_alto=max_alto)
            self.calcular_distancia_centros()
            a = self.calcular_distancia_vertical()
            area = max(self.calcular_superficies())
        print('area2:',area)
        print('area_deseada2:', area_deseada)

    def generar_dispersos_errores(self, min_ancho, max_ancho,min_alto, max_alto, error, area_deseada = 12.5):
        """Garantiza que al menos uno de los dos triangulos generados tiene un área superiror a la
        maxima que puede tener un triangulo aprobado"""
        self.max_ancho = max_ancho
        self.max_alto = max_alto
        self.max_ancho = min_ancho
        self.max_alto = min_alto
        area = 0.0

        if error == 'error_punteria':
            distancia = 100
            diferencia_vertical = 0
            diferencia_horizontal = 0
            while distancia > 4:
                self.clear()
                self.generar_disparos(min_ancho=min_ancho, max_ancho=max_ancho, min_alto=min_alto, max_alto=max_alto)
                distancia = self.calcular_distancia_centros()
        elif error == 'mal_tironeo':
            distancia = 0
            diferencia_vertical = 0
            diferencia_horizontal = 0
            while distancia <4:
                self.clear()
                self.generar_disparos(min_ancho=min_ancho, max_ancho=max_ancho, min_alto=min_alto, max_alto=max_alto)
                distancia = self.calcular_distancia_centros()
            pass
        elif error == 'control_respiracion':
            distancia = 100
            diferencia_vertical = 0
            diferencia_horizontal = 0
            while distancia > 4:
                self.clear()
                self.generar_disparos(min_ancho=min_ancho, max_ancho=max_ancho, min_alto=min_alto, max_alto=max_alto)
                distancia = self.calcular_distancia_centros()
        elif error == 'posicion_inestable':
            distancia = 100
            diferencia_vertical = 0
            diferencia_horizontal = 0
            while distancia > 4:
                self.clear()
                self.generar_disparos(min_ancho=min_ancho, max_ancho=max_ancho, min_alto=min_alto, max_alto=max_alto)
                distancia = self.calcular_distancia_centros()
        elif error == 'deficiente_instruccion':
            distancia = 0
            diferencia_vertical = 0
            diferencia_horizontal = 0
            while distancia < 4:
                self.clear()
                self.generar_disparos(min_ancho=min_ancho, max_ancho=max_ancho, min_alto=min_alto, max_alto=max_alto)
                distancia = self.calcular_distancia_centros()
            pass

        '''
        while area <= area_deseada:
            print(area)
            print(area_deseada)
            self.clear()
            self.generar_disparos(min_ancho=min_ancho, max_ancho=max_ancho,min_alto=min_alto, max_alto=max_alto)

            area = max(self.calcular_superficies())

        print('area2:',area)
        print('area_deseada2:', area_deseada)
        '''
    def calcular_coordenadas(self):
        tanda = list(filter(lambda d: d.indicador == 1, self))
        coord_tanda_1 = list(map(lambda d: d.posicion, tanda))
        tanda = list(filter(lambda d: d.indicador == -1, self))
        coord_tanda_2 = list(map(lambda d: d.posicion, tanda))
        coordenadas = coord_tanda_1, coord_tanda_2
        return coordenadas

    def calcular_distancia_horizontal(self):
        coordenadas = self.calcular_coordenadas()
        coord_tanda_1 = coordenadas[0]
        coord_tanda_2 = coordenadas[1]

        tiro1_tanda1 = coord_tanda_1[0]
        x_tiro1_tanda1 = tiro1_tanda1[0]

        tiro2_tanda1 = coord_tanda_1[1]
        x_tiro2_tanda1 = tiro2_tanda1[0]

        tiro3_tanda1 = coord_tanda_1[2]
        x_tiro3_tanda1 = tiro3_tanda1[0]

        max_x_tanda1 = max(x_tiro1_tanda1, x_tiro2_tanda1, x_tiro3_tanda1)
        min_x_tanda1= min(x_tiro1_tanda1, x_tiro2_tanda1, x_tiro3_tanda1)
        diferencia_tanda1 = max_x_tanda1-min_x_tanda1

        tiro1_tanda2 = coord_tanda_2[0]
        x_tiro1_tanda2 = tiro1_tanda2[0]

        tiro2_tanda2 = coord_tanda_2[1]
        x_tiro2_tanda2 = tiro2_tanda2[0]

        tiro3_tanda2 = coord_tanda_2[2]
        x_tiro3_tanda2 = tiro3_tanda2[0]

        max_x_tanda2 = max(x_tiro1_tanda2, x_tiro2_tanda2, x_tiro3_tanda2)
        min_x_tanda2 = min(x_tiro1_tanda2, x_tiro2_tanda2, x_tiro3_tanda2)
        diferencia_tanda2 = max_x_tanda2 - min_x_tanda2

        diferencia_horizontal = max(diferencia_tanda1, diferencia_tanda2)
        return diferencia_horizontal

    def calcular_distancia_vertical(self):
        coordenadas = self.calcular_coordenadas()
        coord_tanda_1 = coordenadas[0]
        coord_tanda_2 = coordenadas[1]

        tiro1_tanda1 = coord_tanda_1[0]
        y_tiro1_tanda1 = tiro1_tanda1[1]

        tiro2_tanda1 = coord_tanda_1[1]
        y_tiro2_tanda1 = tiro2_tanda1[1]

        tiro3_tanda1 = coord_tanda_1[2]
        y_tiro3_tanda1 = tiro3_tanda1[1]

        max_y_tanda1 = max(y_tiro1_tanda1, y_tiro2_tanda1, y_tiro3_tanda1)
        min_y_tanda1 = min(y_tiro1_tanda1, y_tiro2_tanda1, y_tiro3_tanda1)

        diferencia_tanda1 = max_y_tanda1 - min_y_tanda1
        print(diferencia_tanda1)

        tiro1_tanda2 = coord_tanda_2[0]
        y_tiro1_tanda2 = tiro1_tanda2[0]

        tiro2_tanda2 = coord_tanda_2[1]
        y_tiro2_tanda2 = tiro2_tanda2[0]

        tiro3_tanda2 = coord_tanda_2[2]
        y_tiro3_tanda2 = tiro3_tanda2[0]

        max_y_tanda2 = max(y_tiro1_tanda2, y_tiro2_tanda2, y_tiro3_tanda2)
        min_y_tanda2 = min(y_tiro1_tanda2, y_tiro2_tanda2, y_tiro3_tanda2)
        diferencia_tanda2 = max_y_tanda2 - min_y_tanda2
        print(diferencia_tanda2)

        diferencia_vertical = max(diferencia_tanda1, diferencia_tanda2)
        return diferencia_vertical

    def calcular_distancia_centros(self):
        coordenadas = self.calcular_coordenadas()
        coord_tanda_1 = coordenadas[0]
        coord_tanda_2 = coordenadas[1]

        tiro1_tanda1 = coord_tanda_1[0]
        x_tiro1_tanda1 = tiro1_tanda1[0]
        y_tiro1_tanda1 = tiro1_tanda1[1]

        tiro2_tanda1 = coord_tanda_1[1]
        x_tiro2_tanda1 = tiro2_tanda1[0]
        y_tiro2_tanda1 = tiro2_tanda1[1]

        tiro3_tanda1 = coord_tanda_1[2]
        x_tiro3_tanda1 = tiro3_tanda1[0]
        y_tiro3_tanda1 = tiro3_tanda1[1]

        x_centro_tanda1 = (x_tiro1_tanda1 + x_tiro2_tanda1 + x_tiro3_tanda1) / 3
        y_centro_tanda1 = (y_tiro1_tanda1 + y_tiro2_tanda1 + y_tiro3_tanda1) / 3


        tiro1_tanda2 = coord_tanda_2[0]
        x_tiro1_tanda2 = tiro1_tanda2[0]
        y_tiro1_tanda2 = tiro1_tanda2[1]

        tiro2_tanda2 = coord_tanda_2[1]
        x_tiro2_tanda2 = tiro2_tanda2[0]
        y_tiro2_tanda2 = tiro2_tanda2[1]

        tiro3_tanda2 = coord_tanda_2[2]
        x_tiro3_tanda2 = tiro3_tanda2[0]
        y_tiro3_tanda2 = tiro3_tanda2[1]

        x_centro_tanda2 = (x_tiro1_tanda2 + x_tiro2_tanda2 + x_tiro3_tanda2) / 3
        y_centro_tanda2 = (y_tiro1_tanda2 + y_tiro2_tanda2 + y_tiro3_tanda2) / 3
        print("1:",x_centro_tanda1)
        print('2:',x_centro_tanda2)
        distancia = sqrt(pow((x_centro_tanda2-x_centro_tanda1),2) + pow((y_centro_tanda2-y_centro_tanda1),2))
        print('DISTANCIA:',distancia)
        return distancia

    def calcular_superficies(self):
        if len(self) == 6:
            tanda = list(filter(lambda d: d.indicador == 1, self))
            coord_tanda_1 = list(map(lambda d: d.posicion, tanda))
            tanda = list(filter(lambda d: d.indicador == -1, self))
            coord_tanda_2 = list(map(lambda d: d.posicion, tanda))

            print('coordenada 1:', coord_tanda_1)

            tiro1_tanda1 = coord_tanda_1[0]
            x_tiro1_tanda1 = tiro1_tanda1[0]
            y_tiro1_tanda1 = tiro1_tanda1[1]

            tiro2_tanda1 = coord_tanda_1[1]
            x_tiro2_tanda1 = tiro2_tanda1[0]
            y_tiro2_tanda1 = tiro2_tanda1[1]

            tiro3_tanda1 = coord_tanda_1[2]
            x_tiro3_tanda1 = tiro3_tanda1[0]
            y_tiro3_tanda1 = tiro3_tanda1[1]

            x_centro = (x_tiro1_tanda1+x_tiro2_tanda1+x_tiro3_tanda1)/3
            y_centro = (y_tiro1_tanda1+y_tiro2_tanda1+y_tiro3_tanda1)/3

            tiro1_tanda2 = coord_tanda_1[0]
            tiro2_tanda2 = coord_tanda_1[1]
            tiro3_tanda2 = coord_tanda_1[2]

            superficies = superficie_triangulo(coord_tanda_1), superficie_triangulo(coord_tanda_2)
            return superficies

    def vaciar(self):
        self.clear()

def superficie_triangulo(puntos):
    if len(puntos) == 3:
        A, B, C = puntos
        return abs(0.5 * (A[0] * (B[1] - C[1]) + B[0] * (C[1] - A[1]) + C[0] * (A[1] - B[1])))


if __name__ == "__main__":
    '''
    maximos = []
    impactos = Impactos()
    for i in range(100):
        superficies = []
        for i in range(10000):
            impactos.generar_disparos(max_alto=13, max_ancho=12)
            primer_tanda = list(filter(lambda d : d.indicador == 1, impactos))
            segunda_tanda = list(filter(lambda d: d.indicador == 2, impactos))
            coord_primer_tanda = list(map(lambda d : d.posicion, primer_tanda))
            coord_segunda_tanda = list(map(lambda d: d.posicion, segunda_tanda))
            superficie_primer_tanda = superficie_triangulo(coord_primer_tanda)
            superficie_segunda_tanda = superficie_triangulo(coord_segunda_tanda)
            superficies.append(superficie_primer_tanda)
            superficies.append(superficie_segunda_tanda)
            impactos.clear()
        maximos.append(max(superficies))
    print(max(maximos)) #60.5 si es 12 * 12, 12.5 si es 6 * 6, 2.0 si es 3 * 3
    #Desaprobados:  286 si es 27 * 23, 72 si es 13 * 13, 66 si es 12 * 13
    '''
    impactos = Impactos()
    impactos.generar_dispersos(max_ancho=14, max_alto=14)
    print(impactos)



