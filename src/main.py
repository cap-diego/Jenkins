import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self, str):
        self.assertEqual(str.upper(), str)

if __name__ == '__main__':
    #unittest.TestCase().assertEqual(1, 2)
    TestStringMethods().test_upper('hola')