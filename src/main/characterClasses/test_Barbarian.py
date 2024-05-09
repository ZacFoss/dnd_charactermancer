import unittest

from Barbarian import Barbarian


class testBarbarian(unittest.TestCase):
    def testSetFeatures(self):
        features = Barbarian.setFeatures(self)
        self.assertTrue(features)
        
    def testSetOtherProficiencies(self):
        otherProfs = Barbarian.setOtherProficiencies(self)
        for item in otherProfs:
            print(item['Armor'])
        self.assertTrue(otherProfs)

if __name__ == '__main__':
    unittest.main()