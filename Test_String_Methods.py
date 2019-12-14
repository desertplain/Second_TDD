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
        view = misiek.scen('wyskok', 20)
        self.assertNotEqual(view, view.center(2))

    def test_scou(self):
        view = misiek.scou('Ala ma kota a kot ma ala', 'ma')
        self.assertEqual(view, view.count('ma'))

    def test_senc(self):
        view = misiek.senc('kanalizacja')
        self.assertEqual(view, view.encode())

    def test_ssta(self):
        view = misiek.ssta('Wellcom in Brave New World!', 'Wellcom')
        self.assertTrue(view)

if __name__ == '__main__':
    unittest.main()
