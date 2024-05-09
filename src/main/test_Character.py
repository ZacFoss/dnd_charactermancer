import unittest

from Character import Character
from statObjects.AbilityScore import *


class testCharacter(unittest.TestCase):
    
    def testGenerateCharacter(self):
        character = Character.createCharacter(self)
        print(character.subclass)
        print(character.subrace)
        print(character.features)
        self.assertTrue(character)
        
if __name__ == '__main__':
    unittest.main()
        