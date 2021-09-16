# ここから書いてください

# 状態: name, species, description, weightKg, heightM, isPredator, speedKph, urlPic, registerDate

# 入力例1:
# rabbit = Animal("rabbit", "leporidae", "Rabbits are small mammals in the family Leporidae of the order Lagomorpha (along with the hare and the pika).", 10, 0.3, False, 20, "img1", "2020/5/25")

# 出力例1
# rabbit.getStateString() : "name: rabbit, species: leporidae, description: Rabbits are small mammals in the family Leporidae of the order Lagomorpha (along with the hare and the pika)., weight: 10kg, height: 0.3m, Not Predator, speed: 20kph, urlPic: img1, registerDate: 2020/5/25"
# rabbit.getBmi() : 111.11111111111111
# rabbit.getDailyCalories() : 472.36671315989327
# rabbit.isDangerous() : false

# 入力例2:
# elephant = Animal("elephant", "Elephantidae", "Elephants are mammals of the family Elephantidae and the largest existing land animals.", 300, 3, False, 5, "img2", "2020/5/26")

# 出力例2
# elephant.getStateString() : "name: elephant, species: Elephantidae, description: Elephants are mammals of the family Elephantidae and the largest existing land animals., weight: 300kg, height: 3m, Not Predator, speed: 5kph, urlPic: img2, registerDate: 2020/5/26"
# elephant.getBmi() : 33.333333333333336
# elephant.getDailyCalories() : 6055.08476361958
# elephant.isDangerous() : true
# elephant.isFaster(rabbit) : false

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
        string += "speed: " + self.speedKph + "\n"
        string += "urlPic: " + self.urlPic + "\n"
        string += "registerDate" + self.registerDate + "\n"
        return string
    
    def getBmi(self):
        return self.weightKg / (self.heightM)**2

    def getDailyCalories(self):
        return (70 * (self.weightKg ** 0.75)) * self.activityMultiplier

    
