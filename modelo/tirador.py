import os

from modelo import disparos
from modelo.blanco import Blanco
from modelo.disparos import Impactos





class Tirador:
    def __init__(self):
        self.blancos_usados = []

    def tirar(self,min_ancho, max_ancho, min_alto, max_alto):
        """ Genera los disparos y los impacta en un blanco, el cual guarda el tirador. Los argumendos dan la dispersion
        de los disparos"""
        blanco = Blanco()
        impactos = Impactos()
        try:
            impactos.generar_disparos(min_ancho, max_ancho, min_alto,max_alto)
            blanco.recibir_impactos(impactos)
            self.blancos_usados.append(blanco)
        except disparos.ValueTooSmall:
            print("No se puedo ingresar los impactos.")

    def tirar_mal(self,min_ancho, max_ancho, min_alto, max_alto):
        blanco = Blanco()
        impactos = Impactos()
        try:
            impactos.generar_dispersos(min_ancho, max_ancho, min_alto,max_alto)
            blanco.recibir_impactos(impactos)
            self.blancos_usados.append(blanco)
        except disparos.ValueTooSmall:
            print("No se puedo ingresar los impactos.")

    def tirar_mal_error_punteria(self, min_ancho, max_ancho, min_alto, max_alto):
        blanco = Blanco()
        impactos = Impactos()
        try:
            impactos.generar_dispersos_errores(min_ancho, max_ancho, min_alto, max_alto, error='error_punteria')
            blanco.recibir_impactos(impactos)
            self.blancos_usados.append(blanco)
        except disparos.ValueTooSmall:
            print("No se puedo ingresar los impactos.")

    def tirar_mal_tironeo(self, min_ancho, max_ancho, min_alto, max_alto,):
        blanco = Blanco()
        impactos = Impactos()
        try:
            impactos.generar_dispersos_errores(min_ancho, max_ancho, min_alto, max_alto, error='tironeo')
            blanco.recibir_impactos(impactos)
            self.blancos_usados.append(blanco)
        except disparos.ValueTooSmall:
            print("No se puedo ingresar los impactos.")

    def tirar_mal_control_respiracion(self, min_ancho, max_ancho, min_alto, max_alto,):
        blanco = Blanco()
        impactos = Impactos()
        try:
            impactos.generar_dispersos_errores(min_ancho, max_ancho, min_alto, max_alto, error='control_respiracion')
            blanco.recibir_impactos(impactos)
            self.blancos_usados.append(blanco)
        except disparos.ValueTooSmall:
            print("No se puedo ingresar los impactos.")

    def tirar_mal_posicion_inestable(self, min_ancho, max_ancho, min_alto, max_alto,):
        blanco = Blanco()
        impactos = Impactos()
        try:
            impactos.generar_dispersos_errores(min_ancho, max_ancho, min_alto, max_alto, error='posicion_inestable')
            blanco.recibir_impactos(impactos)
            self.blancos_usados.append(blanco)
        except disparos.ValueTooSmall:
            print("No se puedo ingresar los impactos.")

    def tirar_mal_deficiente_instruccion(self, min_ancho, max_ancho, min_alto, max_alto,):
        blanco = Blanco()
        impactos = Impactos()
        try:
            impactos.generar_dispersos_errores(min_ancho, max_ancho, min_alto, max_alto, error='deficiente_instruccion')
            blanco.recibir_impactos(impactos)
            self.blancos_usados.append(blanco)
        except disparos.ValueTooSmall:
            print("No se puedo ingresar los impactos.")

    def mostrar_blanco(self, index):
        """ Metodo para que el tirador nos muestre en pantalla 1 de los blancos en su poder. """
        self.blancos_usados[index].mostrar_matriz()
        return

    def guardar_blancos(self, foldername:str):
        """ Dado un nombre de carpeta guarda todos los blancos que posee el tirador en esa carpeta """
        try:
            os.mkdir(foldername)
            for index,blanco in enumerate(self.blancos_usados):
                blanco.guardar_csv(f"./{foldername}/blanco_{index}.csv")
        except FileExistsError:
            print("No se puede crear la carpeta por que ya existe")

    def descartar_blancos(self):
        if len(self.blancos_usados) > 0:
            self.blancos_usados.clear()

    def get_datos(self):
        return list(map(lambda b : b.get_datos(), self.blancos_usados))


if __name__ == "__main__":
    tirador = Tirador()
    for _ in range(10):
        tirador.tirar(max_alto=12,max_ancho=12)
    tirador.guardar_blancos("aprobados")
