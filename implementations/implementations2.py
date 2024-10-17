import numpy as np
import heapq

class SimplexHeap:
    def __init__(self, A, b, c):
        """
        Initialise l'algorithme du Simplex avec l'utilisation d'un tas pour gérer les pivots.
        A : Matrice des coefficients des contraintes.
        b : Vecteur des constantes des contraintes.
        c : Coefficients de la fonction objectif.
        """
        self.A = A
        self.b = b
        self.c = c
        self.tableau = self.create_tableau()
        self.heap = []  # Tas pour la gestion des pivots

    def create_tableau(self):
        """
        Crée le tableau initial du Simplex.
        """
        tableau = np.hstack([self.A, np.eye(len(self.A)), self.b.reshape(-1, 1)])
        tableau = np.vstack([tableau, np.hstack([self.c, np.zeros(len(self.b) + 1)])])
        return tableau

    def pivot(self, tableau, row, col):
        """
        Effectue une opération de pivot sur le tableau à l'emplacement (row, col).
        """
        tableau[row] /= tableau[row, col]
        for i in range(len(tableau)):
            if i != row:
                tableau[i] -= tableau[i, col] * tableau[row]
        return tableau

    def is_optimal(self):
        """
        Vérifie si la solution actuelle est optimale.
        """
        return all(val >= 0 for val in self.tableau[-1, :-1])

    def select_pivot_column(self):
        """
        Sélectionne la colonne pivot en utilisant un tas (heap) pour accélérer l'opération.
        """
        heapq.heapify(self.tableau[-1, :-1])  # On crée un tas à partir de la dernière ligne
        pivot_col = np.argmin(self.tableau[-1, :-1])
        return pivot_col

    def select_pivot_row(self, pivot_col):
        """
        Sélectionne la ligne pivot en utilisant la règle du minimum ratio.
        """
        ratios = self.tableau[:-1, -1] / self.tableau[:-1, pivot_col]
        ratios[ratios <= 0] = np.inf
        heapq.heapify(list(ratios))  # Crée un tas pour les ratios
        pivot_row = np.argmin(ratios)
        return pivot_row

    def solve(self):
        """
        Exécute l'algorithme du Simplex pour trouver la solution optimale, en utilisant un tas pour les pivots.
        """
        while not self.is_optimal():
            # Choisir la colonne pivot avec un tas
            pivot_col = self.select_pivot_column()
            if all(self.tableau[:, pivot_col] <= 0):
                raise Exception("Solution non bornée")
            
            # Choisir la ligne pivot (règle du minimum ratio avec un tas)
            pivot_row = self.select_pivot_row(pivot_col)

            # Pivot
            self.tableau = self.pivot(self.tableau, pivot_row, pivot_col)

        return self.tableau[-1, -1], self.tableau

# Exemple d'utilisation
if __name__ == "__main__":
    A = np.array([[1, 1], [2, 1], [1, 2]])
    b = np.array([6, 8, 8])
    c = np.array([-3, -5])

    simplex_heap = SimplexHeap(A, b, c)
    solution, tableau = simplex_heap.solve()
    print("Solution optimale avec tas:", solution)
