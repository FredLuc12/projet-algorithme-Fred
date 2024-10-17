# Analyse des Complexités de l'Algorithme du Simplex

## Implémentation 1 : Utilisation de Matrices Classiques

### Complexité Temporelle
Chaque itération du Simplex implique plusieurs opérations :
- **Choix de la colonne pivot** : O(n), où n est le nombre de variables (colonnes dans le tableau).
- **Choix de la ligne pivot** : O(m), où m est le nombre de contraintes (lignes dans le tableau).
- **Pivotage** : O(m \* n) pour effectuer l'opération de pivot complète.

Dans le pire des cas, l'algorithme peut nécessiter plusieurs itérations avant de trouver la solution optimale.

### Complexité Spatiale
L'algorithme nécessite de stocker un tableau de taille m \* n contenant les coefficients du problème. La complexité spatiale est donc O(m \* n).

## Implémentation 2 : Utilisation d'un Tas (Heap)

### Complexité Temporelle
Cette implémentation optimise les choix des pivots :
- **Choix de la colonne pivot** : O(log n) grâce à l'utilisation d'un tas pour trouver le minimum.
- **Choix de la ligne pivot** : O(log m) avec un tas pour optimiser le calcul du ratio minimum.
- **Pivotage** : O(m \* log n + log m \* n), car l'optimisation ne touche que la sélection des pivots.

### Complexité Spatiale
Similaire à la première implémentation, la complexité spatiale est O(m \* n), car les mêmes données doivent être stockées.

## Conclusion
L'utilisation du tas permet d'améliorer la sélection des pivots, mais l'impact global sur la complexité temporelle dépend du nombre d'itérations. Cette optimisation est particulièrement utile pour les grands problèmes avec de nombreuses variables et contraintes.
