"""
Unit and regression test for the bootcamp_2023 package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import numpy as np

import bootcamp_2023


def test_bootcamp_2023_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "bootcamp_2023" in sys.modules

@pytest.mark.xfail
def test_build_bond_list_exception():
    """Test to see if a faulty bond length errors out"""
    coordinates = np.array([[0, 0, 0], [0, 1, 0]])
    bootcamp_2023.build_bond_list(coordinates, max_bond=0, min_bond=1)
#    with pytest.raises(ValueError):
#        bootcamp_2023.build_bond_list(coordinates, max_bond=0, min_bond=1)

