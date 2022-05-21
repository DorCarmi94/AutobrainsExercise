import unittest

from Main import Main
from WearyArrayTraveler import WearyArrayTraveler
from random import randint
from readers import CSV_reader, TSV_reader, JSON_reader, ProxyReader


class TravelerTestCase(unittest.TestCase):
    def setUp(self):
        self.myTraveler=WearyArrayTraveler()

    def test_wrong_input(self):
        self.assertFalse(self.myTraveler.is_array_traversable([]))
        self.assertFalse(self.myTraveler.is_array_traversable(None))
    def test_only_one_item(self):
        self.assertTrue(self.myTraveler.is_array_traversable([1]))

    def test_basic_case_success(self):
        self.assertTrue(self.myTraveler.is_array_traversable([1,1,1,1]))

    def test_basic_case_fail(self):
        self.assertFalse(self.myTraveler.is_array_traversable([1,1,0,1]))


    def test_known_example_success(self):
        self.assertTrue(self.myTraveler.is_array_traversable([4, 4, 1, 1, 2, 2, 1000, 1]))

    def test_known_example_fail(self):
        self.assertFalse(self.myTraveler.is_array_traversable([4, 2, 1, 3, 2, 2, 1000, 1]))

    def test_random_input_success(self):
        values=dict()
        values[0]=randint(1,100)
        currIdx=0+values[0]
        maxIdx = currIdx
        for i in range(3):
            next=randint(1,100)
            if(currIdx-next<1):
                direction=1
            else:
                direction=randint(1,2)
                if(direction==2):
                    direction=-1
            newPotentialIdx=direction*next+currIdx
            while(newPotentialIdx in values):
                next = randint(1, 100)
                if (currIdx - next < 1):
                    direction = 1
                else:
                    direction = randint(1, 2)
                    if (direction == 2):
                        direction = -1
                newPotentialIdx = direction * next + currIdx

            values[currIdx]=next
            if(newPotentialIdx>maxIdx):
                maxIdx=newPotentialIdx
            currIdx=newPotentialIdx

        values[currIdx]=maxIdx+1 - currIdx

        theArrayToCheck=[]
        for i in range(maxIdx+1):
            if(i in values):
                theArrayToCheck.append(values[i])
            else:
                theArrayToCheck.append(randint(0,1000))

        self.assertTrue(self.myTraveler.is_array_traversable(theArrayToCheck))


    def test_read_from_csv_file(self):
        csvReader=CSV_reader()
        theArray=csvReader.readArrayFromFile("../data/weary_array_traveler_input_example.csv")
        self.assertTrue(len(theArray)>0)
        theArray=csvReader.readArrayFromFile("notANameOfFile.csv")
        self.assertTrue(len(theArray)==0)

    def test_read_from_tsv_file(self):
        tsvReader=TSV_reader()
        theArray=tsvReader.readArrayFromFile("../data/weary_array_traveler_input_example.tsv")
        self.assertTrue(len(theArray)>0)
        theArray=tsvReader.readArrayFromFile("notANameOfFile.tsv")
        self.assertTrue(len(theArray)==0)


    def test_read_from_json_file(self):
        jsonReader=JSON_reader()
        theArray=jsonReader.readArrayFromFile("../data/weary_array_traveler_input_example.json")
        self.assertTrue(len(theArray)>0)
        theArray=jsonReader.readArrayFromFile("notANameOfFile.tsv")
        self.assertTrue(len(theArray)==0)

    def test_proxy_reader_read_file(self):
        reader=ProxyReader()
        theArray = reader.readArrayFromFile("../data/weary_array_traveler_input_example.json")
        self.assertTrue(len(theArray) > 0)

        theArray = reader.readArrayFromFile("../data/weary_array_traveler_input_example.csv")
        self.assertTrue(len(theArray) > 0)

        theArray = reader.readArrayFromFile("../data/weary_array_traveler_input_example.tsv")
        self.assertTrue(len(theArray) > 0)


    def test_main(self):
        main=Main()
        main.readFromFileAndCheckTravel("../data/weary_array_traveler_input_example.json")
        self.assertTrue(len(main.theLastArray)>0)
        self.assertTrue(main.theLastAnswer)

        main.readFromFileAndCheckTravel("../data/weary_array_traveler_input_example.csv")
        self.assertTrue(len(main.theLastArray) > 0)
        self.assertTrue(main.theLastAnswer)

        main.readFromFileAndCheckTravel("../data/weary_array_traveler_input_example.tsv")
        self.assertTrue(len(main.theLastArray) > 0)
        self.assertTrue(main.theLastAnswer)



