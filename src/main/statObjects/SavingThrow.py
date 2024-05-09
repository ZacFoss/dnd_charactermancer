from statObjects.AbilityScore import AbilityScore


class SavingThrow:
    def __init__(self, name, modifier, proficient):
        self.name = name
        self.modifier = modifier
        self.proficient = proficient
    
    def setSavingThrow(savingThrow, abilityScore, additionalModifier):
        savingThrow = AbilityScore.setAbilityScoreModifier(abilityScore) + additionalModifier
        
    def isProficient(self):
        return self.proficient
    
    def setAllSavingThrows(self, abilityScores, profBonus, profSavingThrows):
        savingThrows = []
        
        for x in abilityScores:
            if AbilityScore.getName(x) in profSavingThrows:
                savingThrow = SavingThrow(AbilityScore.getName(x), AbilityScore.setAbilityScoreModifier(AbilityScore.getScore(x) + profBonus), True)
            else:
                savingThrow = SavingThrow(AbilityScore.getName(x), AbilityScore.setAbilityScoreModifier(AbilityScore.getScore(x)), False)
            savingThrows.append(savingThrow)
            
        return savingThrows
    
    def getName(self):
        return self.name
    
    def getModifier(self):
        return self.modifier