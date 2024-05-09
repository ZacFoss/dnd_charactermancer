import unittest

from AbilityScore import AbilityScore


class testAbilityScores(unittest.TestCase):
    
    # def setUp(self):
    #     self.abilityScores = AbilityScore(0,0,0,0,0,0)
    #     self.abilityScores2 = AbilityScore(16,0,0,0,0,0)
    
    def testGenerateScore(self):
        self.assertNotEqual(AbilityScore.generateScore(self), 0, "Assert Is not Equal to 0")
        
    # def testSetAbilityScoreModifier(self):
    #     self.assertEqual(AbilityScore.setAbilityScoreModifier(self.abilityScores2, self.abilityScores2.strength), 3)
    
    def testGenerateAllScores(self):
        test = AbilityScore.generateAllScores(self)
        for x in test:
            self.assertIsNotNone(AbilityScore.getName(x))
            self.assertIsNotNone(AbilityScore.getScore(x))
        
if __name__ == '__main__':
    unittest.main()