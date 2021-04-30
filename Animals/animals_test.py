from Mammals import Mammals
from Birds import Birds
from Reptiles import Reptiles 
import unittest

class TestAnimals(unittest.TestCase):

    def test_mammals(self):
        mammals = Mammals()
        self.assertEqual(['Tiger', 'Elephant', 'Wild Cat'], mammals.get_mammals())

    def test_Birds(self):
        birds = Birds()
        self.assertEqual(['Sparrow', 'Robin', 'Duck'], birds.get_birds())

    def test_Reptiles(self):
        reptiles = Reptiles()
        self.assertEqual(['Lizard', 'Snake', 'Turtle'], reptiles.get_Reptiles())

    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())
    #
    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

if __name__ == '__main__':
    unittest.main()
