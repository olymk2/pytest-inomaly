# -*- coding: utf-8 -*-
import os
import pytest
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

    group.addoption(
        '--update',
        action='store',
        dest='update_images',
        default=False,
        help='Test images have changed, so replace with current results, should be visually tested first'
    )


def pytest_configure(config):
    pytest.update_images = config.getoption('update_images')
    pytest.idiff = idiff
    pytest.idiff_variance = idiff_variance


def compare_images(actual_results, expected_results):
    do_assets_exist(actual_results, expected_results)
    # Make diffed results positive
    diff = abs(imread(actual_results).astype(float) - imread(expected_results).astype(float))

    # L1 Norm:(Taxicab norm or Manhattan norm)
    l1_norm = sum(diff)

    # L0-norm :Total number of non-zero elements in a vector. It is a cardinality function
    l0_norm = norm(diff.ravel(), 0)

    return l0_norm / diff.size


def do_assets_exist(actual_results, expected_results):
    if not os.path.exists(expected_results):
        raise IOError

    if pytest.update_images is True:
        with open(actual_results, 'r') as actual_file:
            with open(expected_results, 'w') as expected_file:
                expected_file.write(actual_result.read())

    if not os.path.exists(actual_results):
        raise IOError


def idiff(actual_results, expected_results, tolerance=0.0):
    norm = compare_images(
        actual_results='%s' % actual_results,
        expected_results='%s' % expected_results)
    if norm <= tolerance:
        return True
    return False


def idiff_variance(actual_results, expected_results, tolerance=0.0):
    return compare_images(
        actual_results='%s' % actual_results,
        expected_results='%s' % expected_results)
