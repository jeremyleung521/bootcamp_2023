"""
Unit and regression test for the bootcamp_2023.measure module.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import numpy as np

import bootcamp_2023


def test_calculate_distance():
    """
    Test if calculated output from calculate_distance() matches expected output.
    """
    r1 = np.array([0,0,0])
    r2 = np.array([0,1,0])
    expected_dist = 1.0

    calculated_dist = bootcamp_2023.calculate_distance(r1, r2)

    assert expected_dist == calculated_dist


