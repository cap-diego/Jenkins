import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self, str):
        self.assertEqual(str.upper(), str)
        
def test_always_fails():
    TestStringMethods().test_upper('asd')

def test_always_success():
    TestStringMethods().test_upper('HOLA')

if __name__ == '__main__':
    #unittest.TestCase().assertEqual(1, 2)
    test_always_success()
    try:
        test_always_fails()
    except:
        print("Test falló")