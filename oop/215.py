import math
import math
class Planet:
    constantOfGravitation = 6.67438 * (10 ** -11)
    speedOfLight = 2.99792458 * (10 ** 8)
    massOfSun = 1.989 * (10 ** 30)
    radiumOfSun = 6.96 * (10 ** 5)
    oneYear = 31556926
    def __init__(self, massKg, meanRadiumKm, distanceToStarLs):
        self.massKg = massKg
        self.meanRadiumKm = meanRadiumKm
        self.distanceToStarLs = distanceToStarLs

    def getVolume(self):
        return 4/3 * (self.meanRadiumKm ** 3) * math.pi
    
    def getSurfaceArea(self):
        return 4 * (self.meanRadiumKm ** 2) * math.pi

    def compareToPlanet(self, planet):
        ctp = getVolume(self) - getVolume(planet)
        return ctp

        



