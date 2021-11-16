class File:
    def __init__(self, fileName, fileExtension, content, locked, parentFolder):
        self.fileName = fileName
        self.fileExtension = fileExtension
        self.content = content
        self.locked = locked
        self.parentFolder = parentFolder

    def getLifetimeBandwithSize(self):
        return str(len(self.content) * 10) + "MB"

    def getFileType(self):
        if self.fileExtension == ".pdf" or self.fileExtension == ".word" or self.fileExtension == ".txt": return "document"
        elif self.fileExtension == ".js" or self.fileExtension == ".css" or self.fileExtension == ".html" : return "source-code"
        elif self.fileExtension == ".mp4" : return "mp4"
        elif self.fileExtension == ".mp3" : return "music"
    
    def prependContent(self, data):
        if self.locked == False:
            self.content = data + self.content
            return self.content

    def showFileLocation(self):
        return self.parentFolder + ">" + self.fileName + self.fileExtension
