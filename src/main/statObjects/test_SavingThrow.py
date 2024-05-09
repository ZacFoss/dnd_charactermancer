import unittest

from AbilityScore import AbilityScore
from SavingThrow import SavingThrow


class testSavingThrow(unittest.TestCase):
    
    def setUp(self):
        self.savingThrow1 = SavingThrow("Strength", 4, False)
        self.savingThrow2 = SavingThrow("Strength", 1, True)
        self.abilityScore1 = AbilityScore(15, "Dexterity")
        self.abilityScore2 = AbilityScore(12, "Strength")
        self.abilityScores = [self.abilityScore1, self.abilityScore2]
        
    def testIsProficient(self):
        self.assertEqual(False, SavingThrow.isProficient(self.savingThrow1))
        self.assertEqual(True, SavingThrow.isProficient(self.savingThrow2))
        
    def testSetAllSavingThrows(self):
        testSavingThrowArray = SavingThrow.setAllSavingThrows(self.savingThrow1, self.abilityScores)
        
        for x in testSavingThrowArray:
            if(SavingThrow.getName(x) == "Dexterity"):
                self.assertEqual(2, SavingThrow.getModifier(x))
            else:
                self.assertEqual("Strength", SavingThrow.getName(x))
                self.assertEqual(1, SavingThrow.getModifier(x))

if __name__ == '__main__':
    unittest.main()