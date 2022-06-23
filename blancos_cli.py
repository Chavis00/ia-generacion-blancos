#!/usr/bin/env python
import argparse
import csv
from os import listdir
from os.path import isfile, join



from modelo import tirador

def validar_int_args(arg:int, max:int):
    return arg > 2 and arg <= max

def validar_csv():
    #TODO: Implementar un algoritmo que valide que los CSV tengan los tiros adecuados.
    pass

def generar_archivo(nombre_archivo):
    # nombre_archivo: es el nombre que tiene la carpeta de la cual quiero concatenar los archivos.
    # archivo: el csv de blanco que estoy trabajando.
    with open(nombre_archivo + ".csv","w", newline='') as nuevo:
        archivos = [f for f in listdir("./" + nombre_archivo) if isfile(join("./" + nombre_archivo, f))]
        for archivo in archivos:
            with open(nombre_archivo + "/" + archivo, "r") as blanco:
                reader = csv.reader(blanco)
                for fila in reader:
                    nuevo.write(",".join(fila))
                    nuevo.write(",")
                # nuevo.write(aprobado o desaprobado)
                nuevo.write("\n")
                
                    



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(dest="directorio", type=str,
                        help="Directorio donde se guardarán los CSV de blancos generados. No debe existir en .")
    parser.add_argument(dest="max_alto", type=int,
                        help="Alto máximo de la dispersion de los disparos, no puede ser menor a 3 unidades ni puede ser"
                             " mayor a la altura de la matriz del blanco o sea 28 unidades.")
    parser.add_argument(dest="max_ancho", type=int,
                        help="Ancho máximo de la dispersion de los disparos, no puede ser menor a 3 unidades ni puede "
                             "ser mayor a la anchura de la matriz del blanco o sea 24 unidades.")
    args = parser.parse_args()
    if validar_int_args(args.max_alto, 28) and validar_int_args(args.max_ancho, 24):
        tirador = tirador.Tirador()
        for _ in range(10):
            # Ancho y alto es la dispersion de los disparos
            # 12 por 12 representa aprobado en la tabla de calificacion
            # La ubicacion en el blanco y dentro de la dispersion
            # son aleatorio con distr uniforme
            tirador.tirar(max_alto=args.max_alto, max_ancho=args.max_ancho)
        tirador.guardar_blancos(args.directorio)
        # generar_archivo(args.directorio)
    else:
        print("Ancho o alto incorrecto. --help para ayuda.")
