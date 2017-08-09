# -*- coding: utf-8 -*-
import os
import pytest


def test_file_exists():
    test_directory = os.path.abspath(os.path.dirname(__file__))
    with pytest.raises(IOError):
        result = pytest.idiff(
            '%s/fixture/doesnotexist.png' % (test_directory),
            '%s/fixture/original.png' % (test_directory))

        result = pytest.idiff(
            '%s/fixture/original.png' % (test_directory),
            '%s/fixture/doesnotexist.png' % (test_directory))


def test_help_message(testdir):
    result = testdir.runpytest(
        '--help',
    )
    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        'Inomaly:',
        '*--serve=DEST_FOO*Set the value for the fixture "bar".',
    ])


