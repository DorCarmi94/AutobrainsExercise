from numpy import loadtxt
import json
class Reader:
    def readArrayFromFile(self,pathToFile):
        return []


class JSON_reader(Reader):
    def readArrayFromFile(self,pathToFile):
        try:
            with open(pathToFile,'rb') as file:
                json_array=json.load(file)
                return json_array
        except Exception as ex:
            print(ex)
            return []

class CSV_reader:
    def readArrayFromFile(self, pathToFile):
        try:
            with open(pathToFile,'rb') as file:
                data = loadtxt(file,dtype=int, delimiter=",")
                return data.tolist()
        except Exception as ex:
            print(ex)
            return []

class TSV_reader(Reader):
    def readArrayFromFile(self,pathToFile):
        try:
            with open(pathToFile, 'rb') as file:
                data = loadtxt(file, dtype=int, delimiter="\t")
                return data.tolist()
        except Exception as ex:
            print(ex)
            return []


class ProxyReader(Reader):
    def __init__(self):
        self.reader=Reader()

    def determineReader(self,endingOfPath):
        if(endingOfPath=='csv'):
            self.reader=CSV_reader()
        elif(endingOfPath=='tsv'):
            self.reader=TSV_reader()
        elif(endingOfPath=='json'):
            self.reader = JSON_reader()

    def readArrayFromFile(self,pathToFile):
        if(not isinstance(pathToFile,str)):
            print("Wrong path to file: type not string")
            return []

        splitedString=pathToFile.split(".")
        if(len(splitedString)<2):
            print("Wrong path to file: wrong ")
            return []

        endingOfPath=splitedString[-1]

        self.determineReader(endingOfPath)
        return self.reader.readArrayFromFile(pathToFile)