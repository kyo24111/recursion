class File:

    def __init__(self,fileName, fileExtension, content, locked, parentFolder):
        self.fileName = fileName
        self.fileExtension = fileExtension
        self.content = content
        self.locked = locked
        self.parentFolder = parentFolder

    # サービス中に使われるファイルの最大容量を返します。
    def getLifetimeBandwidthSize(self):
        return str(len(self.content) * 10) + "MB"

    # オブジェクトのファイルタイプを返します。document(.pdf, .word, .txt)、source-code(.js, .css, .html)、video(.mp4)、music(.mp3)
    def getFileType(self):
        if self.fileExtension == ".pdf" or self.fileExtension == ".word" or self.fileExtension == ".txt": return "document"
        elif self.fileExtension == ".js" or self.fileExtension == ".css" or self.fileExtension == ".html": return "source-code"
        elif self.fileExtension == ".mp4": return "video"
        elif self.fileExtension == ".mp3": return "music"

    # もしファイルがロックされていなければ、ファイルのcontentの先頭にデータ文字列を追加し、新しいcontentを返します。
    def prependContent(self, data):
        if self.locked == False: self.content = data + self.content
        return self.content

    # もしファイルがロックされていなければ、ファイルのcontentの末尾にデータ文字列を追加し、新しいcontentを返します。
    def appendContent(self, data):
        if self.locked == False: self.content += data
        return self.content

    # もしファイルがロックされていなければ、ファイルのcontentの指定した位置(インデックス)にデータ文字列を追加し、新しいcontentを返します。
    def addContent(self,data, position):
        if self.locked == False:
            self.content = self.content[0: position] + data + self.content[position: len(self.content)]
        return self.content

    # 親ファイル > ファイル名.拡張子という形で返します。
    def showFileLocation(self):
        return self.parentFolder + " > " + self.fileName + self.fileExtension

assignment = File("assignment", ".word", "Something that occurs too early before preparations are ready. Starting too soon.", False, "homework")

print(assignment.getLifetimeBandwidthSize())
print(assignment.getFileType())
print(assignment.prependContent("good morning "))
print(assignment.appendContent(" good evening"))
print(assignment.addContent("hello world ", 13))
print(assignment.showFileLocation())