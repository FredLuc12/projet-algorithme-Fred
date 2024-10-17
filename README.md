# Projet Algorithme du Simplex

## Description
Ce projet implémente l'algorithme du Simplex pour résoudre des problèmes d'optimisation linéaire. Nous avons créé deux versions :
1. **Implémentation avec des matrices classiques** pour les opérations de pivot.
2. **Implémentation avec un tas (heap)** pour optimiser la sélection des pivots.

## Structure du Projet
Le projet est organisé comme suit :
projet-algorithme-arielle/ ├── README.md ├── main.py ├── descriptions/ │ └── description_simple.md ├── implementations/ │ ├── implementation1.py │ └── implementation2.py ├── tests/ │ ├── test_implementation1.py │ └── test_implementation2.py ├── visualisations/ │ └── visualisation.py ├── analyses/ │ └── analyse_complexite.md └── ressources/


## Exécution du projet
### Installation des dépendances
Assurez-vous d'installer **numpy** et **matplotlib** pour exécuter les implémentations et visualisations :
```bash
pip install numpy matplotlib

# Lancer l'algorithme
Vous pouvez exécuter l'algorithme avec la commande suivante :

python main.py

# Visualisation
Pour visualiser l'algorithme du Simplex en action, exécutez le script suivant :

python visualisations/visualisation.py
# Exécuter les tests
Pour exécuter les tests unitaires, utilisez pytest :

pytest tests/

# Analyse des Complexités 
Pour plus d'informations sur la comparaison des performances des deux implémentations, consultez le fichier analyse_complexite.md.

# Licence
Projet réalisé par Fred Ablefonlin dans le cadre d'un exercice d'implémentation d'algorithmes en Python.


---




