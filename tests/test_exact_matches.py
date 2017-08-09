# -*- coding: utf-8 -*-
import os
import pytest
from pytest_inomaly import idiff


def test_exact_identical_images_idiff(testdir):
    test_directory = os.path.abspath(os.path.dirname(__file__))
    result = pytest.idiff(
        '%s/fixture/original.png' % (test_directory),
        '%s/fixture/original.png' % (test_directory))
    assert result is True


def test_exact_pixel_diference_images_idiff(testdir):
    test_directory = os.path.abspath(os.path.dirname(__file__))
    result = pytest.idiff(
        '%s/fixture/original.png' % (test_directory),
        '%s/fixture/pixel.png' % (test_directory))
    assert result is False


def test_exact_glitch_diference_images_idiff(testdir):
    test_directory = os.path.abspath(os.path.dirname(__file__))
    result = pytest.idiff(
        '%s/fixture/original.png' % (test_directory),
        '%s/fixture/glitch.png' % (test_directory))
    assert result is False


def test_exact_color_diference_images_idiff(testdir):
    test_directory = os.path.abspath(os.path.dirname(__file__))
    result = pytest.idiff(
        '%s/fixture/original.png' % (test_directory),
        '%s/fixture/different_colors.png' % (test_directory))
    assert result is False


def test_exact_rotated_diference_images_idiff(testdir):
    test_directory = os.path.abspath(os.path.dirname(__file__))
    result = pytest.idiff(
        '%s/fixture/original.png' % (test_directory),
        '%s/fixture/rotated.png' % (test_directory))
    assert result is False
