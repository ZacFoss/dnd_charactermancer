from math import *
from random import *


class AbilityScore:
    def __init__(self, score, name):
        self.score = score
        self.name = name
        
    def setAbilityScoreModifier(abilityScore):
        return floor((abilityScore - 10)/2)
            
    def generateScore(self):
        numbers = []
        score = 0
        for x in range(4):
            numbers.append(int(randrange(1,6)))
        for _ in range(1):
            m = min(numbers)
            numbers[:] = (x for x in numbers if x != m)
        for x in numbers:
            score = score + x
        
        return score
        
    def generateAllScores(self):
        abilityScores = []
        listOfAbilities = ["Strength", "Dexterity", "Constitution", "Wisdom", "Intelligence", "Charisma"]
        
        for x in listOfAbilities:
            abilityScore = AbilityScore(score=AbilityScore.generateScore(self), name=x)
            abilityScores.append(abilityScore)
            
        return abilityScores
    
    def getScore(self):
        return self.score
    
    def getName(self):
        return self.name