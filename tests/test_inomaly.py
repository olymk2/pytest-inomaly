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


def test_hello_ini_setting(testdir):
    testdir.makeini("""
        [pytest]
        HELLO = world
    """)

    testdir.makepyfile("""
        import pytest

        @pytest.fixture
        def hello(request):
            return request.config.getini('HELLO')

        def test_hello_world(hello):
            assert hello == 'world'
    """)

    result = testdir.runpytest('-v')

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        '*::test_hello_world PASSED',
    ])

    # make sure that that we get a '0' exit code for the testsuite
    assert result.ret == 0
