import pytest
from dz_14 import Tree


t = Tree(6)

def test_is_contains_element_True():
     assert t.is_contains_element(6) == True

def test_is_contains_element_False():
    assert t.is_contains_element(4) == False

def test_insert():
    t.insert(4)
    assert t.is_contains_element(4) == True

def test_append_list():
    t.append_list([1, 8, 10])
    assert t.is_contains_element(1) and t.is_contains_element(8) and t.is_contains_element(10) == True

def test_get_min_node():
    assert t.get_min_node() == 1

def test_get_max_node():
    assert t.get_max_node() == 10

def test_delete_node():
    t.delete_node(t, 6)
    assert t.is_contains_element(6) == False








