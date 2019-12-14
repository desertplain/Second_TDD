import unittest
import misiek

class Test_String(unittest.TestCase):

    def test_scap(self):
        view = misiek.scap('rzeczy')
        self.assertEqual(view, view.capitalize())

    def test_scas(self):
        view = misiek.scas('strachy na lachy')
        self.assertEqual(view, view.casefold())

    def test_scen(self):
        view = misiek.scen('wyskok', 2)
        self.assertEqual(view, view.center())

    def test_scou(self):
        view = misiek.scou('Ala ma kota a kot ma ala', 'ma')
        self.assertEqual(view, view.count())

    def test_senc(self):
        view = misiek.senc('kanalizacja')
        self.assertEqual(view, view.encode())

if __name__ == '__main__':
    unittest.main()
