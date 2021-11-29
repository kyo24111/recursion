import datetime
currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
year = date.strftime("%Y")
print(date)
print(year)
class User:
    def __init__(self, username, firstName, lastName, email, passwordHashed, birthMonth, birthYear, biographyDescription, favoriteHikingLocation):
        self.username = username
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.passwordHashed = passwordHashed
        self.birthMonth = birthMonth
        self.birthYear = birthYear
        self.biographyDescription = biographyDescription
        self.favoriteHikingLocation = favoriteHikingLocation
        
    def getFullName(self):
        return self.firstName + " " + self.lastName

    def getAge(self):
        currentYear = datetime.datetime.now().year
        currentMonth = datetime.datetime.now().month
        result = currentYear - self.birthYear
        return result if currentMonth >= self.birthMonth else result -1
    
    def birthdayCalculator(self):
        currentMonth = datetime.datetime.now().month
        if currentMonth - self.birthMonth > 0: return 12 - (currentMonth - self.birthMonth)
        else: return self.birthMonth - currentMonth
    
    def showProfile(self):
        return self.username + "\n" + str(self.getAge()) + "years old\n" + self.biographyDescription + "\nfavorite place to hike: " + self.favoriteHikingLocation
    
    def confirmPassword(self, passwordString):
        return self.passwordString ==