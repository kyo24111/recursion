import datetime
class User:
     
    def __init__(self, username, firstName, lastName, email, passwordString, birthMonth, birthYear, biographyDescription, favoriteHikingLocation):
        
        self.username = username
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.passwordString = HelperFunction.hashPassword(passwordString)
        self.birthMonth = birthMonth
        self.birthYear = birthYear
        self.biographyDescription = biographyDescription
        self.favoriteHikingLocation = favoriteHikingLocation
    # ユーザーのフルネームを返します。
    def getFullName(self):
        return self.firstName + " " + self.lastName

    # ユーザーの年齢を返します。
    def getAge(self):
        currentYear = datetime.datetime.now().year
        currentMonth = datetime.datetime.now().month
        result = currentYear - self.birthYear
        return result if currentMonth >= self.birthMonth else result - 1

    # 誕生日まであと何ヶ月あるか計算して返します。
    def birthdayCalculator(self):
        currentMonth = datetime.datetime.now().month
        if currentMonth - self.birthMonth > 0: return 12 - (currentMonth - self.birthMonth)
        else: return self.birthMonth - currentMonth

    # ユーザーのプロフィールを返します。
    def showProfile(self):
        return self.username + "\n" + str(self.getAge()) + " years old\n" + self.biographyDescription + "\nfavorite place to hike: " + self.favoriteHikingLocation

    # 指定したpasswordStringが保存したpasswordStringと一致しているかをブーリアン値で返します。
    # セキュリティのために、パスワードのハッシュ化されたバージョンがメモリ内の状態に保存されることに注意してください。
    def confirmPassword(self, passwordString):
        return self.passwordString == HelperFunction.hashPassword(passwordString)

class HelperFunction:    
    # パスワードを文字列として受け取り、その文字列をマップし、ハッシュ化されたパスワードhashedPassword返します。
    def hashPassword(passwordstring):
        hash = 5381
        for x in passwordstring:
           hash = (( hash << 5) + hash) + ord(x)
        return str(hash & 0xFFFFFFFF)

claire = User("claireS", "Claire", "Simmons", "clairesimmons@gmail.com", "lmnlmn", 9, 2007, "Passionate gamer. Evil internet aficionado. Student. Friendly tv specialist. Introvert.", "Hollywood Sign Hike")

print(claire.getFullName())
print(claire.getAge())
print(claire.birthdayCalculator())
print(claire.showProfile())
print(claire.confirmPassword("lmnlmn"))
print(HelperFunction.hashPassword("lmnlmn")) # passwordをハッシュ化