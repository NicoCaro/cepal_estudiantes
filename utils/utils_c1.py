import matplotlib.pyplot as plt
import numpy as np

def grafica_inicialización(df, centroides):
    # Inicializa figura
    plt.figure(figsize=(8, 8))
    
    # grafica puntos
    plt.plot(df[:,1], df[:,0], 'o', alpha=.7, label="países")
    
    # grafica centroides
    plt.plot(centroides[:,1], centroides[:,0], 'x', ms=14, label="centroides")
    
    # Agregar títulos a los ejes
    plt.xlabel("Índice de Capacidad Estadística", fontsize=12)
    plt.ylabel("Índice de Desarrollo Humano", fontsize=12)
    plt.legend()
    plt.title("Inicialización de centroides", fontsize=16)
    
    plt.show()
    

def grafica_kmeans(df, centroides, clust, n_iter):
    # Inicializar figura
    plt.figure(figsize=(8,8))
    
    # Graficar cada uno de los clusters con diferentes colores
    for j, color in enumerate(plt.cm.Dark2( np.linspace(0, 1, centroides.shape[0]))):
        plt.plot(df[clust == j,1], df[clust == j,0], 'o', color=color)
        plt.plot(centroides[j,1], centroides[j,0], 'x', ms=14, color=color,
                label="Cluster %d" % j)
        
    # Agregar títulos a los ejes
    plt.xlabel("Índice de Capacidad Estadística", fontsize=12)
    plt.ylabel("Índice de Desarrollo Humano", fontsize=12)
    plt.legend()
    plt.title("K-Means: iteración %d" % n_iter, fontsize=16)
    plt.show()
    