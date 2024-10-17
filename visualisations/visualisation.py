import numpy as np
import matplotlib.pyplot as plt

def plot_simplex(A, b, c):
    """
    Visualise le processus de l'algorithme du Simplex pour un problème en deux dimensions.
    A : Matrice des contraintes.
    b : Vecteur des constantes des contraintes.
    c : Coefficients de la fonction objectif.
    """

    # Définir les variables d'axes
    x = np.linspace(0, 10, 400)

    # Tracer les contraintes
    for i in range(len(A)):
        plt.plot(x, (b[i] - A[i, 0] * x) / A[i, 1], label=f'Contrainte {i+1}')

    # Ajouter des axes, des labels et des titres
    plt.xlim(0, 10)
    plt.ylim(0, 10)
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.title('Visualisation de l\'algorithme du Simplex')
    plt.legend()

    # Tracer la fonction objectif pour quelques valeurs de z
    for z in range(0, 20, 5):
        plt.plot(x, (z - c[0] * x) / c[1], linestyle='--', color='gray')

    plt.show()

# Exemple d'utilisation
if __name__ == "__main__":
    A = np.array([[1, 1], [2, 1], [1, 2]])
    b = np.array([6, 8, 8])
    c = np.array([-3, -5])
    
    plot_simplex(A, b, c)
