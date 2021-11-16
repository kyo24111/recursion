class Tax:
    def __init__(self, name, federalTax, stateTax, localTax):
        self.name = name
        self.federalTax = federalTax
        self.stateTax = stateTax
        self.localTax = localTax
        
class DownloadableProduct:
    def __init__(self, title, description, price, sizeMb, extension):
        self.title = title
        self.description = description
        self.price = price
        self.sizeMb = sizeMb
        self.extension = extension
    
    def getFinalPrice(self, taxObject):
        return self.price + (self.price * taxObject.federalTax) + (self.price * taxObject.stateTax) + (self.price * taxObject.localTax)


product1 = DownloadableProduct("A hero returns - Remasterd", "A movie about a hero who saves the world", 23.5, 13000, "mp4")
taxLasVegas = Tax("Las Vegas Taxes", 0.02, 0.05, 0.01)
# print(taxLasVegas.name)

print(product1.title + "'s price is:" + str(product1.price))
print(product1.title + "'s final price for " + taxLasVegas.name + " is: " + str(product1.getFinalPrice(taxLasVegas)))