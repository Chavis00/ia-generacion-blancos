import numpy as np
import matplotlib.pyplot as plt
from modelo import tirador

def heatmap(data, row_labels, col_labels, ax=None,
            cbar_kw={}, cbarlabel="", **kwargs):
    """
    Create a heatmap from a numpy array and two lists of labels.

    Parameters
    ----------
    data
        A 2D numpy array of shape (N, M).
    row_labels
        A list or array of length N with the labels for the rows.
    col_labels
        A list or array of length M with the labels for the columns.
    ax
        A `matplotlib.axes.Axes` instance to which the heatmap is plotted.  If
        not provided, use current axes or create a new one.  Optional.
    cbar_kw
        A dictionary with arguments to `matplotlib.Figure.colorbar`.  Optional.
    cbarlabel
        The label for the colorbar.  Optional.
    **kwargs
        All other arguments are forwarded to `imshow`.
    """

    if not ax:
        ax = plt.gca()

    # Plot the heatmap
    im = ax.imshow(data, **kwargs)

    # Create colorbar
    cbar = ax.figure.colorbar(im, ax=ax, **cbar_kw)
    cbar.ax.set_ylabel(cbarlabel, rotation=-90, va="bottom")

    # We want to show all ticks...
    ax.set_xticks(np.arange(data.shape[1]))
    ax.set_yticks(np.arange(data.shape[0]))
    # ... and label them with the respective list entries.
    ax.set_xticklabels(col_labels)
    ax.set_yticklabels(row_labels)

    # Let the horizontal axes labeling appear on top.
    ax.tick_params(top=True, bottom=False,
                   labeltop=True, labelbottom=False)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=-30, ha="right",
             rotation_mode="anchor")

    # Turn spines off and create white grid.
    for edge, spine in ax.spines.items():
        spine.set_visible(False)

    ax.set_xticks(np.arange(data.shape[1]+1)-.5, minor=True)
    ax.set_yticks(np.arange(data.shape[0]+1)-.5, minor=True)
    ax.grid(which="minor", color="w", linestyle='-', linewidth=3)
    ax.tick_params(which="minor", bottom=False, left=False)
    plt.savefig('plot.png', dpi=300, bbox_inches='tight')
    plt.show()
    return im, cbar

FILAS = list(range(1, 29))
COLUMNAS = list(range(1, 25))
if __name__ == "__main__":


    # Generar un blanco aprobado y graficarlo
    tirador = tirador.Tirador()
    tirador.tirar(max_alto=6,max_ancho=6)
    aprobado = np.array(tirador.get_datos()[0], dtype=float)
    heatmap(aprobado, FILAS, COLUMNAS)

    # Generar un blanco desaprobado y graficarlo
    tirador.tirar_mal(max_ancho=23, max_alto=27)
    desaprobado = np.array(tirador.get_datos()[1], dtype=float)
    heatmap(desaprobado, FILAS, COLUMNAS)
    tirador.descartar_blancos()

    # Mostrar acumulados de n tiros
    acumulados = np.zeros((28,24))
    for _ in range(20000):
        tirador.tirar(12,12)
        acumulados += np.abs(np.array(tirador.get_datos()[0], dtype=float))
        tirador.descartar_blancos()

    heatmap(acumulados, FILAS, COLUMNAS)

    acumulados = np.zeros((28, 24))
    for _ in range(20000):
        tirador.tirar_mal(max_ancho=24, max_alto=28)
        acumulados += np.abs(np.array(tirador.get_datos()[0], dtype=float))
        tirador.descartar_blancos()

    heatmap(acumulados, FILAS, COLUMNAS)

