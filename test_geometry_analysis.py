"""
Tests for geometry analysis functions from geom_analysis.py code
"""

import geom_analysis as ga

# function name needs to start with 'test'
def test_calculate_distance():
    coord1 = [0, 0, 0]
    coord2 = [1, 0, 0]
    
    expected = 1.0
    observed = ga.calculate_distance(coord1, coord2)
    
    # we'll make an assert statement which makes sure that they are indeed equal
    # if it is, the test will pass
    
    assert observed == expected
    
# let's now try to write a test script to test the function, bond_check
def test_bond_check():
    distance = 0.3
    
    expected = True
    observed = ga.bond_check(distance)
    
    assert observed == expected
       
# What about bond_check at edge values? Like 0 or 1.5

def test_bond_check_0():
    distance = 0
    expected = False
    observed = ga.bond_check(distance)
    assert observed == expected
    
def test_bond_check_1p6():
    distance = 1.6
    expected = False
    observed = ga.bond_check(distance)
    assert observed == expected
    
    
