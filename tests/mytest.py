__author__ = 'Davide Monfrecola'

from unittest import TestCase

class PhantomRestClientTest(TestCase):

    def setUp(self):
        self.foo = 2

    def test_client(self):
        # test
        self.assertEqual(self.foo, 2)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
