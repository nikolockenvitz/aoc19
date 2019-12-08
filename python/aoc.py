
PATH_INPUT  = "../input/"
PATH_OUTPUT = "../output/"
IOFILE_PREFIX = ""
IOFILE_DAYFORMAT = "02d"
IOFILE_SUFFIX = ".txt"

PATH_COOKIES = "../cookies.txt"
PATH_CONFIG = "../config.txt"

import hashlib
import sys
import os
import re
import urllib.request
import time

class AOC:
    def __init__(self, day):
        self.day = day
        print("# "*10 + "Day "+str(self.day) + " #"*10)

        # Filename of input- and output-file
        filename = self.getIOFilenameForDay(self.day)
        self.filenameInput  = PATH_INPUT  + filename
        self.filenameOutput = PATH_OUTPUT + filename

    @classmethod
    def getIOFilenameForDay(cls, day):
        filename = IOFILE_PREFIX
        filename+= format(day, IOFILE_DAYFORMAT)
        filename+= IOFILE_SUFFIX
        return filename

    @classmethod
    def getDayFromFilepath(cls, filepath):
        filename = os.path.basename(filepath)
        numbers = re.findall("\d+", filename)
        firstNumber = int(numbers[0])
        return firstNumber

    @classmethod
    def getTodaysPythonScriptFilename(cls):
        localtime = time.localtime()
        return "day" + format(localtime.tm_mday, IOFILE_DAYFORMAT) + ".py"

    @classmethod
    def createTodaysPythonScript(cls):
        f = open("day00.py", "r")
        templateContent = f.read()
        f.close()

        todaysFilename = cls.getTodaysPythonScriptFilename()

        if(os.path.exists(todaysFilename)):
            print("Today's script does already exist.")
        else:
            f = open(todaysFilename, "w")
            f.write(templateContent)
            f.close()

    @classmethod
    def openTodaysPythonScript(cls):
        todaysFilename = cls.getTodaysPythonScriptFilename()

        try:
            f = open(PATH_CONFIG, "r")
            pythonPath = f.read()
            f.close()
        except:
            pythonPath = sys.executable

        command = 'START "" "{python}" -m idlelib "{file}" {file}'
        command = command.format(python=pythonPath, file=todaysFilename)

        filename = "_start.bat"
        f = open(filename, "w")
        f.write(command)
        f.close()

        os.system(filename)

    @classmethod
    def saveTodaysInputToFile(cls):
        url = cls.getTodaysInputUrl()

        try:
            data = cls.getWebsiteData(url)
            cls.__saveTodaysInputToFile(data)
            print("Saved input!")
        except urllib.error.HTTPError as e:
            print("Failed to get today's input...")
            print(e)
            localtime = time.localtime()
            if (localtime.tm_hour == 5):
                diff = (59 - localtime.tm_min) * 60 + (60 - localtime.tm_sec)
                print("Will try again in " + str(diff) + " seconds")
                time.sleep(diff)
                cls.saveTodaysInputToFile()
            elif (localtime.tm_hour == 6):
                print("Will try again in 1 second...")
                time.sleep(1)
                cls.saveTodaysInputToFile()
            else:
                input("Press Enter to exit")

    @classmethod
    def getTodaysInputUrl(cls):
        localtime = time.localtime()
        urlTemplate = "https://adventofcode.com/{YEAR}/day/{DAY}/input"
        url = urlTemplate.format(YEAR = localtime.tm_year,
                                 DAY  = localtime.tm_mday)
        return url

    @classmethod
    def getWebsiteData(cls, url):
        cookies = cls.getCredentialCookies()

        opener = urllib.request.build_opener()
        for cookie in cookies:
            opener.addheaders.append(('Cookie', cookie))

        response = opener.open(url)
        return response.read().decode()

    @classmethod
    def getCredentialCookies(cls):
        f = open(PATH_COOKIES)
        cookies = f.read().splitlines()
        f.close()
        return cookies

    @classmethod
    def __saveTodaysInputToFile(cls, data):
        filename = cls.getIOFilenameForDay(time.localtime().tm_mday)
        f = open(PATH_INPUT + filename, "w")
        f.write(data)
        f.close()

    """
    Input/Output
    """
    def getFile(self, readLines=False):
        f = open(self.filenameInput, "r")
        if(readLines):
            content = f.read().splitlines()
        else:
            content = f.read().strip()
        f.close()
        return content

    def getFileLines(self):
        return self.getFile(readLines=True)

    def output(self, result1, result2, printTerminal=True):
        if(printTerminal):
            print("Result1:", result1)
            print("Result2:", result2)
        f = open(self.filenameOutput, "w")
        f.write(str(result1))
        f.write("\n")
        f.write(str(result2))
        f.close()
        
        if(printTerminal and "idlelib" not in sys.modules): input("")

    """
    Hash
    """
    def hash(self, function, text):
        oHash = function()
        oHash.update(text.encode())
        return oHash.hexdigest()

    def hashSHA1(self, text):
        return self.hash(hashlib.sha1, text)

    def hashSHA256(self, text):
        return self.hash(hashlib.sha256, text)

    def hashSHA512(self, text):
        return self.hash(hashlib.sha512, text)

    def hashMD5(self, text):
        return self.hash(hashlib.md5, text)

    """
    Other basic operations
    """
    def copyList(self, list1):
        newList = []
        for element in list1:
            if(type(element) == list):
                element = self.copyList(element)
            newList.append(element)
        return newList


if __name__ == "__main__":
    AOC.createTodaysPythonScript()
    AOC.openTodaysPythonScript()
    AOC.saveTodaysInputToFile()
