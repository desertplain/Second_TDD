import unittest
import misiek

class Test_String(unittest.TestCase):

    def test_scap(self):
        zd='rzeczy'
        view = misiek.scap(zd)
        self.assertEqual(view, zd.capitalize())

    def test_scas(self):
        zd='strachy na lachy'
        view = misiek.scas(zd)
        self.assertEqual(view, zd.casefold())

    def test_scen(self):
        zd='wyskok'
        ilo=20
        view = misiek.scen(zd,ilo)
        self.assertEqual(view,zd.center(ilo))

    def test_scou(self):
        zd1='Ala ma kota a kot ma ala'
        zd2='ma'
        view = misiek.scou(zd1,zd2)
        self.assertEqual(view, zd1.count(zd2))

    def test_senc(self):
        zd='kanalizacja'
        view = misiek.senc(zd)
        self.assertEqual(view, zd.encode())

    def test_ssta(self):
        view = misiek.ssta('Wellcom in Brave New World!', 'Wellcom')
        self.assertTrue(view)

if __name__ == '__main__':
    unittest.main()
