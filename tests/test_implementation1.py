import pytest
import numpy as np
from implementations.implementations1 import Simplex

def test_simple_case():
    A = np.array([[1, 1], [2, 1], [1, 2]])
    b = np.array([6, 8, 8])
    c = np.array([-3, -5])
    simplex = Simplex(A, b, c)
    solution, _ = simplex.solve()
    assert solution == pytest.approx(11.0), "Test simple échoué"

def test_unbounded_solution():
    A = np.array([[1, -1], [-1, 1]])
    b = np.array([1, -1])
    c = np.array([1, -1])
    simplex = Simplex(A, b, c)
    with pytest.raises(Exception):
        simplex.solve()

def test_edge_case():
    A = np.array([[0, 1], [1, 0]])
    b = np.array([0, 0])
    c = np.array([0, 0])
    simplex = Simplex(A, b, c)
    solution, _ = simplex.solve()
    assert solution == pytest.approx(0.0), "Test limite échoué"
