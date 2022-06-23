import numpy as np
from plot_disparos import heatmap, FILAS, COLUMNAS

"""
blanco1 = np.zeros((28, 24))
blanco1[6][11] = -1
blanco1[12][13] = -1
blanco1[15][13] = -1

blanco1[10][13] = 1
blanco1[13][10] = 1
blanco1[14][15] = 1

if __name__ == "__main__":
    heatmap(blanco1, FILAS, COLUMNAS)
"""
#Blanco A: Aprobado
blancoA = np.zeros((28, 24))
blancoA[10][11] = -1
blancoA[12][13] = -1
blancoA[15][11] = -1

blancoA[10][13] = 1
blancoA[13][10] = 1
blancoA[14][15] = 1


#Blanco B: error de punteria
blancoB = np.zeros((28, 24))
blancoB[7][11] = -1
blancoB[10][14] = -1
blancoB[13][9] = -1

blancoB[4][17] = 1
blancoB[6][14] = 1
blancoB[9][19] = 1


#Blanco C: Tironeo
blancoC = np.zeros((28, 24))
blancoC[5][8] = -1
blancoC[15][20] = -1
blancoC[25][6] = -1

blancoC[3][16] = 1
blancoC[12][2] = 1
blancoC[21][16] = 1


#Blanco D: control de respiración
blancoD = np.zeros((28, 24))
blancoD[5][7] = -1
blancoD[11][10] = -1
blancoD[22][3] = -1

blancoD[6][9] = 1
blancoD[14][3] = 1
blancoD[20][10] = 1


#Blanco E: posición inestable
blancoE = np.zeros((28, 24))
blancoE[17][4] = -1
blancoE[20][10] = -1
blancoE[15][18] = -1

blancoE[16][9] = 1
blancoE[19][1] = 1
blancoE[18][15] = 1


#Blanco F: Deficiente instrucción
blancoF = np.zeros((28, 24))
blancoF[2][11] = -1
blancoF[12][23] = -1
blancoF[20][15] = -1

blancoF[12][12] = 1
blancoF[20][1] = 1
blancoF[26][13] = 1

if __name__ == "__main__":
    heatmap(blancoA, FILAS, COLUMNAS)
    heatmap(blancoB, FILAS, COLUMNAS)
    heatmap(blancoC, FILAS, COLUMNAS)
    heatmap(blancoD, FILAS, COLUMNAS)
    heatmap(blancoE, FILAS, COLUMNAS)
    heatmap(blancoF, FILAS, COLUMNAS)
