Python import system example
----------------------------

This code provides an example of how to set up a package and make use of the Python import system. This is not meant to be a best practices guide, it is only a summary of what has worked for me. I hope you find it helpful :D

Testing
-------

To run the tests:

    pip install -r requirements.txt 
    py.test test.py

If you want to inspect a failing test, with objects from each test available to you, run the tests with:

    py.test --pdb test.py

Often times I find it useful to write a test as failing:

    def test_something():
        # bring in an object here and start testing it
        # add code as necessary to get your tests to pass
        assert False

I find this pattern nice to iteratively edit and add code.

Mocking
-------

Another common thing when testing is mocking. There is an example in `test.py` of how to do that when using `requests.get`. The `mock` library seems to be a very powerful tool for this purpose.

The basic idea is to mock the behavior of an object your code depends on. AFAIK you only need to mock the parts of the object required to test your code paths.

Refs
----
+ Test-Driven Development with Python by HJW Percival
+ pytest docs
+ mock documentation from python stdlib