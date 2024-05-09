import json
from math import *
from random import *


class Barbarian:
    def __init__(self, features):
        self.features = features
        
    def setFeatures(self):
        barbarianFile = open("project/main/characterClasses/featuresBarbarian.json", "r")
        barbariandata = barbarianFile.read()
        features = json.loads(barbariandata)
        return features
    
    def setOtherProficiencies(self):
        otherProficienciesFile = open("project/main/characterClasses/proficiencies.json", "r")
        otherProficiencyData = otherProficienciesFile.read()
        otherProfs = json.loads(otherProficiencyData)
        return otherProfs
            
        