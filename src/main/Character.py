from random import randint

from characterClasses.Barbarian import *
from statObjects.AbilityScore import *
from statObjects.SavingThrow import *


class Character:
    
    def __init__(self, level: int, abilityScores, savingThrows, features,
                charClass, charRace, profSkills, proficiencies, equipment,
                profBonus, profSavingThrows, skills, age, size, speed, subclass,
                subrace, background):
        self.level = level
        self.abilityScores = abilityScores
        self.savingThrows = savingThrows
        self.features = features
        self.charClass = charClass
        self.charRace = charRace
        self.proficiencies = proficiencies
        self.equipment = equipment
        self.profBonus = profBonus
        self.profSkills = profSkills
        self.profSavingThrows = profSavingThrows
        self.skills = skills
        self.age = age
        self.size = size
        self.speed = speed
        self.subclass = subclass
        self.subrace = subrace
        self.background = background
        
        
    def createCharacter(self):
        self.level = randint(3, 3)
        self.charClass = Character.randomizeClass(self)
        self.charRace = Character.randomizeRace(self)
        self.background = Character.randomizeBackground(self)
        self.skills = [
            {
                "Skill": "Athletics",
                "Ability": "Strength"
            },
            {
                "Skill": "Acrobatics",
                "Ability": "Dexterity"
            },
            {
                "Skill": "Sleight of Hand",
                "Ability": "Dexterity"
            },
            {
                "Skill": "Stealth",
                "Ability": "Dexterity"
            },
            {
                "Skill": "Arcana",
                "Ability": "Intelligence"
            },
            {
                "Skill": "History",
                "Ability": "Intelligence"
            },
            {
                "Skill": "Investigation",
                "Ability": "Intelligence"
            },
            {
                "Skill": "Nature",
                "Ability": "Intelligence"
            },
            {
                "Skill": "Religion",
                "Ability": "Intelligence"
            },
            {
                "Skill": "Animal Handling",
                "Ability": "Wisdom"
            },
            {
                "Skill": "Insight",
                "Ability": "Wisdom"
            },
            {
                "Skill": "Medicine",
                "Ability": "Wisdom"
            },
            {
                "Skill": "Perception",
                "Ability": "Wisdom"
            },
            {
                "Skill": "Survival",
                "Ability": "Wisdom"
            },
            {
                "Skill": "Deception",
                "Ability": "Charisma"
            },
            {
                "Skill": "Initimidation",
                "Ability": "Charisma"
            },
            {
                "Skill": "Performance",
                "Ability": "Charisma"
            },
            {
                "Skill": "Persuasion",
                "Ability": "Charisma"
            }
        ]
        Character.setFromJSON(self, self.charClass, self.charRace, self.level)
        self.features = Character.setFeatures(self, self.features, self.subclass, self.subrace, self.level)
        self.abilityScores = AbilityScore.generateAllScores(self)
        self.savingThrows = SavingThrow.setAllSavingThrows(self, self.abilityScores, self.profBonus, self.profSavingThrows)
        Character.setSkills(self, self.skills, self.profSkills, self.profBonus, self.abilityScores)
        return self
    
    def randomizeClass(self):
        classes = ["barbarian"]
        index = randint(0, len(classes) - 1)
        return classes[index]
    
    def randomizeRace(self):
        races = ["dwarf"]
        index = randint(0, len(races) - 1)
        return races[index]
    
    def randomizeBackground(self):
        backgrounds = ["Acolyte"]
        index = randint(0, len(backgrounds) - 1)
        return backgrounds[index]
    
    def setFromJSON(self, charClass, charRace, level):
        file = open("src/main/classJSON/" + charClass + ".json", "r")
        data = file.read()
        data = json.loads(data)
        for item in data:
            self.features = item['Features']
            self.proficiencies = item['Proficiencies']
            self.equipment = item['Equipment']
            self.profBonus = item['Proficiency Bonus'][level - 1]
            self.profSkills = sample(item['Skills'], 2)
            self.profSavingThrows = item['Saving Throws']
            self.subclass = sample(item["Subclasses"], 1)[0]
            
        file = open("src/main/raceJSON/" + charRace + ".json", "r")
        data = file.read()
        data = json.loads(data)
        for item in data:
            self.age = item['Age']
            self.size = item['Size']
            self.speed = item['Speed']
            self.features = self.features + item['Features']
            self.subrace = sample(item['Subraces'], 1)[0]
            
    def setSkills(self, skillList, profSkills, profBonus, abilityScore): # type: ignore
        for skill in skillList:
            if skill['Skill'] in profSkills:
                for score in abilityScore:
                    if AbilityScore.getName(score) == skill['Ability']:
                        skill['Modifier'] = AbilityScore.setAbilityScoreModifier(AbilityScore.getScore(score)) + profBonus
                        skill['Proficient'] = True
            else:
                for score in abilityScore:
                    if AbilityScore.getName(score) == skill['Ability']:
                        skill['Modifier'] = AbilityScore.setAbilityScoreModifier(AbilityScore.getScore(score))
                        skill['Proficient'] = False
                        
    def setFeatures(self, features, subclass, subrace, level):
        return [feature for feature in features if feature['level'] <= level
                and (("subclass" not in feature and "subrace" not in feature)
                    or ("subclass" not in feature and feature['subrace'] == subrace)
                    or ("subrace" not in feature and feature['subclass'] == subclass))]