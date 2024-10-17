import numpy as np
from implementations.implementations1 import Simplex
from implementations.implementations2 import SimplexHeap

def run_simplex_implementation1():
    print("Exécution de l'implémentation 1 du Simplex (Matrices classiques)")
    # Définir un exemple simple d'optimisation linéaire
    A = np.array([[1, 1], [2, 1], [1, 2]])
    b = np.array([6, 8, 8])
    c = np.array([-3, -5])
    
    # Créer une instance de Simplex
    simplex = Simplex(A, b, c)
    
    # Résoudre et afficher la solution
    solution, tableau = simplex.solve()
    print("Solution optimale (implémentation 1) :", solution)
    print("Tableau final :", tableau)

def run_simplex_implementation2():
    print("Exécution de l'implémentation 2 du Simplex (Tas)")
    # Définir un exemple simple d'optimisation linéaire
    A = np.array([[1, 1], [2, 1], [1, 2]])
    b = np.array([6, 8, 8])
    c = np.array([-3, -5])
    
    # Créer une instance de SimplexHeap
    simplex_heap = SimplexHeap(A, b, c)
    
    # Résoudre et afficher la solution
    solution, tableau = simplex_heap.solve()
    print("Solution optimale (implémentation 2) :", solution)
    print("Tableau final :", tableau)

if __name__ == "__main__":
    # Exécuter l'une des implémentations
    print("Choisissez une implémentation :")
    print("1. Implémentation 1 (Matrices classiques)")
    print("2. Implémentation 2 (Tas)")
    
    choice = input("Entrez votre choix (1 ou 2) : ")
    
    if choice == "1":
        run_simplex_implementation1()
    elif choice == "2":
        run_simplex_implementation2()
    else:
        print("Choix invalide.")
