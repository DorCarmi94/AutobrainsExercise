from WearyArrayTraveler import WearyArrayTraveler
from readers import ProxyReader


class Main:
    def __init__(self):
        self.reader=ProxyReader()
        self.traveler=WearyArrayTraveler()
        self.theLastArray=[]
        self.theLastAnswer=False
    def readFromFileAndCheckTravel(self,pathToFile):
        self.theLastArray=self.reader.readArrayFromFile(pathToFile)
        self.theLastAnswer=self.traveler.is_array_traversable(self.theLastArray)


if __name__=='__main__':
    main=Main()
    print("Please enter path to file with array (CSV/TSV/JSON):")
    path=input()
    if(path is None or len(path)<1):
        print("Bad input")

    main.readFromFileAndCheckTravel(path)

    print("The array is:")
    print(main.theLastArray)
    print("The answer is:")
    print(main.theLastAnswer)