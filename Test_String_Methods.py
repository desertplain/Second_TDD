import unittest
import string

class Test_String(unittest.TestCase):

    def test_scap(self):
        view = string.scap()
        self.assertEqual(view, capitalize(view))

if __name__ == '__main__':
    unittest.main()
