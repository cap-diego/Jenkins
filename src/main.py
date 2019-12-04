import unittest
import argparse

class TestStringMethods(unittest.TestCase):

    def test_isupper_always_true(self):
        self.assertTrue('HOLA'.isupper())
    #
    # def test_isupper_always_false(self):
    #     self.assertTrue('hola'.isupper())

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('job_id')
    args = parser.parse_args()
    print("Running case with job ID: {}".format(args.job_id))
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)

