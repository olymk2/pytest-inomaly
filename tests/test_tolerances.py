# -*- coding: utf-8 -*-
import os
import pytest


def test_exact_antialiasing_difference(testdir):
    test_directory = os.path.abspath(os.path.dirname(__file__))
    result = pytest.idiff(
        '%s/fixture/100x100-cube.png' % (test_directory),
        '%s/fixture/100x100-cube-antialias-01.png' % (test_directory),
        tolerance=0.05)
    assert result is True


def test_exact_extreme_difference(testdir):
    test_directory = os.path.abspath(os.path.dirname(__file__))
    result = pytest.idiff(
        '%s/fixture/100x100-cube-white.png' % (test_directory),
        '%s/fixture/100x100-cube-black.png' % (test_directory),
        tolerance=0.05)
    assert result is False


def test_exact_identical_images_idiff(testdir):
    test_directory = os.path.abspath(os.path.dirname(__file__))

    result = pytest.idiff(
        '%s/fixture/100x100-cube.png' % (test_directory),
        '%s/fixture/100x100-cube.png' % (test_directory),
        tolerance=0.05)
    assert result is True

    result = pytest.idiff(
        '%s/fixture/original.png' % (test_directory),
        '%s/fixture/original.png' % (test_directory),
        tolerance=0.05)
    assert result is True


def test_exact_pixel_diference_images_idiff(testdir):
    test_directory = os.path.abspath(os.path.dirname(__file__))

    result = pytest.idiff(
        '%s/fixture/100x100-cube.png' % (test_directory),
        '%s/fixture/100x100-cube-pixel-difference.png' % (test_directory),
        tolerance=0.05)
    assert result is True

    result = pytest.idiff(
        '%s/fixture/original.png' % (test_directory),
        '%s/fixture/pixel.png' % (test_directory),
        tolerance=0.05)
    assert result is True


def test_exact_glitch_diference_images_idiff(testdir):
    test_directory = os.path.abspath(os.path.dirname(__file__))

    #small image with glitch large enough to  detect
    result = pytest.idiff(
        '%s/fixture/100x100-cube.png' % (test_directory),
        '%s/fixture/100x100-cube-glitch-line.png' % (test_directory),
        tolerance=0.1)
    assert result is False

    # much larger images so difference is not big enough to detect
    result = pytest.idiff(
        '%s/fixture/original.png' % (test_directory),
        '%s/fixture/glitch.png' % (test_directory),
        tolerance=0.1)
    assert result is True


def test_exact_color_diference_images_idiff(testdir):
    test_directory = os.path.abspath(os.path.dirname(__file__))

    result = pytest.idiff(
        '%s/fixture/100x100-cube.png' % (test_directory),
        '%s/fixture/100x100-cube-color-difference.png' % (test_directory),
        tolerance=0.1)
    assert result is False

    result = pytest.idiff(
        '%s/fixture/original.png' % (test_directory),
        '%s/fixture/different_colors.png' % (test_directory),
        tolerance=0.1)
    assert result is False


def test_exact_rotated_diference_images_idiff(testdir):
    test_directory = os.path.abspath(os.path.dirname(__file__))
    result = pytest.idiff(
        '%s/fixture/original.png' % (test_directory),
        '%s/fixture/rotated.png' % (test_directory),
        tolerance=0.1)
    assert result is False
