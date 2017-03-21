# -*- coding: utf-8 -*-
import os
import pytest
import scipy
from numpy import array, float64, concatenate
from scipy.misc import imread
from scipy.linalg import norm


def pytest_addoption(parser):
    group = parser.getgroup('Inomaly')
    group.addoption(
        '--serve',
        action='store',
        dest='dest_foo',
        default='2017',
        help='Set the value for the fixture "bar".'
    )

    parser.addini('HELLO', 'Dummy pytest.ini setting')


def compare_images(image_path1, image_path2):
    # file_fixture_path = '%s' % image1
    # file_actual_path = '%s' % image2

    do_assets_exist(image_path1, image_path2)
    # Make diffed results positive
    diff = abs(imread(image_path1).astype(float) - imread(image_path2).astype(float))

    # L1 Norm:(Taxicab norm or Manhattan norm)
    l1_norm = sum(diff)

    # L0-norm :Total number of non-zero elements in a vector. It is a cardinality function
    l0_norm = norm(diff.ravel(), 0)

    print(l0_norm / diff.size)
    return l0_norm / diff.size


def do_assets_exist(image_path1, image_path2):
    if not os.path.exists(image_path1):
        raise IOError
    if not os.path.exists(image_path2):
        raise IOError


def pytest_namespace():
    def idiff(image_path1, image_path2, tolerance=0.0):
        norm = compare_images(
            image_path1 = '%s' % image_path1,
            image_path2 = '%s' % image_path2)
        if norm <= tolerance:
            return True
        return False

    def idiff_variance(image_path1, image_path2, tolerance=0.0):
        return compare_images(
            image_path1 = '%s' % image_path1,
            image_path2 = '%s' % image_path2)

    return {'_assumption_locals': [],
            '_failed_assumptions': [],
            'idiff': idiff}

