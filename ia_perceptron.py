from traceback import print_tb
from modelo import tirador
import numpy as np
from sklearn.neural_network import MLPClassifier
import time
from tqdm import tqdm

from blancos_reales import blancoA as blanco1





if __name__ == "__main__":
    tirador = tirador.Tirador()
    clasificacion = []
    CANT_DATOS = 75000
    i=0
    for _ in tqdm(range(15000)):
        tirador.tirar(min_ancho=0, max_ancho=6, min_alto=0, max_alto=6)
        clasificacion.append(1) # Lo clasificamos como 1 "Aprobado"
        tirador.tirar_mal_error_punteria(min_ancho=18, max_ancho=24, min_alto=18, max_alto=24)
        clasificacion.append(5)
        tirador.tirar_mal_tironeo(min_ancho=0, max_ancho=24, min_alto=0, max_alto=24)
        clasificacion.append(2)
        tirador.tirar_mal_control_respiracion(min_ancho=18, max_ancho=24, min_alto=0, max_alto=24)
        clasificacion.append(3)
        tirador.tirar_mal_posicion_inestable(min_ancho=0, max_ancho=24, min_alto=18, max_alto=28)
        clasificacion.append(4)
        # Lo clasificamos como 0 "Desaprobado"
        i = i+1

    # Metemos los datos en numpy arrays y los acomodamos
    matriz_datos = np.array(tirador.get_datos(), dtype=float)
    matriz_clasificacion = np.array(clasificacion, dtype=float)
    print(matriz_clasificacion)
    # Aplanamos los datos
    matriz_datos= matriz_datos.reshape(CANT_DATOS, 28 * 24)
    # Creamos el perceptron y lo entrenamos
    inicio = time.time()
    clf = MLPClassifier(solver='adam', activation="tanh",max_iter=1200, random_state=4,
                        hidden_layer_sizes=(972//6,972//9,972//12), verbose=True)
    clf = clf.fit(matriz_datos, matriz_clasificacion)
    tirador.descartar_blancos()

    
    # Prueba de prediccion de buen desempeño
    CANT_PRUEBA = 100



    # Hago 10 Blancos aprobados
    print("PRUEBA BUENA")
    for _ in range(CANT_PRUEBA):
        tirador.tirar(min_ancho=0, max_alto=6, min_alto=0, max_ancho=6)
        #tirador.guardar_blancos(foldername='buena')
        prueba = tirador.get_datos()
    matriz_prueba = np.array(prueba, dtype=float)
    matriz_prueba = matriz_prueba.reshape(CANT_PRUEBA, 28 * 24)
    list = clf.predict(matriz_prueba).tolist()
    print(f'Acertó {list.count(1.0)} de {CANT_PRUEBA} blancos aprobados.')
    tirador.descartar_blancos()


    #PRUEBA DE ERROR DE PUNTERIA
    print("PRUEBA DE ERROR DE PUNTERIA")
    i = 0
    for _ in range(CANT_PRUEBA):
        i+1
        tirador.tirar_mal_error_punteria(min_ancho=18, max_ancho=24, min_alto=18, max_alto=24)
        prueba = tirador.get_datos()

    matriz_prueba = np.array(prueba, dtype=float)
    matriz_prueba = matriz_prueba.reshape(CANT_PRUEBA, 28 * 24)
    list = clf.predict(matriz_prueba).tolist()  
    print(f'Acertó {list.count(5.0)}  de {CANT_PRUEBA} blancos desaprobados por error de punteria.')


    tirador.descartar_blancos()
    

    #PRUEBA DE TIRONEO
    print("PRUEBA DE TIRONEO")
    for _ in range(CANT_PRUEBA):
        tirador.tirar_mal_tironeo(min_ancho=0, max_ancho=24, min_alto=0, max_alto=24)
        #tirador.guardar_blancos(foldername='tironeo')
        prueba = tirador.get_datos()

    matriz_prueba = np.array(prueba, dtype=float)
    matriz_prueba = matriz_prueba.reshape(CANT_PRUEBA, 28 * 24)
    list = clf.predict(matriz_prueba).tolist()    
    print(f'Acertó {list.count(2.0)}  de {CANT_PRUEBA} blancos desaprobados por tironeo.')
    tirador.descartar_blancos()




    #PRUEBA MAL RESPIRACION
    print("PRUEBA MAL RESPIRACION")
    for _ in range(CANT_PRUEBA):
        tirador.tirar_mal_control_respiracion(min_ancho=18, max_ancho=24, min_alto=0, max_alto=24)
        #tirador.guardar_blancos(foldername='respiracion')
        prueba = tirador.get_datos()
    matriz_prueba = np.array(prueba, dtype=float)
    matriz_prueba = matriz_prueba.reshape(CANT_PRUEBA, 28 * 24)
    list = clf.predict(matriz_prueba).tolist()   
    print(f'Acertó {list.count(3.0)}  de {CANT_PRUEBA} blancos desaprobados por mala respiracion.')
    tirador.descartar_blancos()


    #PRUEBA INESTABLE
    print("PRUEBA INESTABLE")
    for _ in range(CANT_PRUEBA):
        tirador.tirar_mal_posicion_inestable(min_ancho=0, max_ancho=24, min_alto=18, max_alto=28)
        #tirador.guardar_blancos(foldername='inestable')
        prueba = tirador.get_datos()

    matriz_prueba = np.array(prueba, dtype=float)
    matriz_prueba = matriz_prueba.reshape(CANT_PRUEBA, 28 * 24)
    list = clf.predict(matriz_prueba).tolist()    
    print(f'Acertó {list.count(4.0)}  de {CANT_PRUEBA} blancos desaprobados por inestabilidad')
    tirador.descartar_blancos()


    fin = time.time()
    tiempo_total = fin - inicio
    print(f'TIEMPO TOTAL: {tiempo_total}s')
    blanco1 = blanco1.reshape(1, 28 * 24)

#OUTPUT DE EJEMPLO
#Acertó 58.0 de 100 blancos aprobados.
#Acertó 58.0 de 100 blancos desaprobados.