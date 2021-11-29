class Animal:
    activityMultiplier = 1.2

    def __init__(self, name, species, description, weightKg, heightM, isPredator, speedKph, urlPic, registerDate):
        self.name = name
        self.species = species
        self.description = description
        self.weightKg = weightKg
        self.heightM = heightM
        self.isPredator = isPredator
        self.speedKph = speedKph
        self.urlPic = urlPic
        self.registerDate = registerDate

    def getStateString(self):
        string = ''
        string += "name: " + self.name + "\n"
        string += "species: " + self.species + "\n"
        string += "description: " + self.description + "\n"
        string += "weight: " + str(self.weightKg) + "\n"
        string += "height: " + str(self.heightM) + "\n"
        string += ("Predator" if self.isPredator == True else "Not Predator") + "\n"
        string += "speed: " + str(self.speedKph) + "\n"
        string += "urlPic: " + self.urlPic + "\n"
        string += "registerDate" + self.registerDate + "\n"
        return string

    def getBmi(self):
        return self.weightKg / (self.heightM)**2

    def getDailyCalories(self):
        return (70 * (self.weightKg ** 0.75)) * self.activityMultiplier

    def isDangerouns(self):
        if self.isPredator == True or self.heightM >= 1.7 or self.speedKph >= 35:
            return True
        else:
            return False

    def isFaster(self, animal):
        if self.speedKph >= animal.speedKph:
            return True
        else:
            return False

rabbit = Animal("rabbit", "leporidae", "this is rabbit", 10, 0.3, False, 20, "img1", "2020/5/25")
elephant = Animal("elephant", "Elephantidae", "this is elephant", 300, 3, False, 5, "img2", "2020/5/26")

print(rabbit.getStateString())
print(rabbit.getDailyCalories())
