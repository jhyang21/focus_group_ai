class Persona:
    def __init__(self, name, age, race_ethnicity, education_level, income, priorities, values):
        self.name = name
        self.age = age
        self.race_ethnicity = race_ethnicity
        self.education_level = education_level
        self.income = income
        self.priorities = priorities
        self.values = values
    
    def __str__(self):
        return f"{self.name}{self.age}"
    
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
    def getRaceEthnicity(self):
        return self.race_ethnicity
    
    def getEducationLevel(self):
        return self.education_level
    
    def getIncome(self):
        return self.income
    
    def getPriorities(self):
        return self.priorities
    
    def getValues(self):
        return self.values