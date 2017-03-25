pytest-Inomaly
===================================

[![Build Status](https://ci.digitaloctave.com/api/badges/oly/pytest-inomaly/status.svg)](https://ci.digitaloctave.com/oly/pytest-inomaly)

A simple image diff plugin for pytest currently provides two new methods, use full for testing image related code and making sure the results do not change unexpectedly.

 - pytest.idiff - returns true or false 
 - pytest.idiff_variance - returns the difference between the two images
     
     
Requirements
------------
Requires scipy and pytest to calculate the differences.

 - scipy
 - pytest


Installation
------------

You can install "pytest-Inomaly" via `pip`_ from `PyPI`_::

    $ pip install pytest-Inomaly


Usage
-----


Assert images are identical.

    assert idiff(path_to_first_image, path_to_second_image) is True

Assert images are almost identical, allow some variation for anti aliasing or similar.

    assert idiff(path_to_first_image, path_to_second_image, tolerance=0.1) is True

Same as the above two method but will return the difference as a value instead of true or false.

    assert idiff_tolerance(path_to_first_image, path_to_second_image, tolerance=0.1) == 3.14


Contributing
------------
Contributions are very welcome. Tests can be run with `tox`_, please ensure
the coverage at least stays the same before you submit a pull request.

License
-------

Distributed under the terms of the `MIT`_ license, "pytest-Inomaly" is free and open source software


Issues
------

If you encounter any problems, please `file an issue`_ along with a detailed description.
