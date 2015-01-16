__author__ = 'Davide Monfrecola'

import unittest

class PhantomRestClientTest(unittest.TestCase):

    def setUp(self):
        self.foo = 2

    def test_client(self):
        # test
        self.assertEqual(self.foo, 2)

if __name__ == '__main__':
    unittest.main()
