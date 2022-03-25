
import pickle

def main():
    fileName = "DegreesDict.dat"
    dictionary = getDictionary(fileName)
    printSortedDict(dictionary)
    

def getDictionary(fileName):
    infile = open(fileName, 'rb')
    degrees = pickle.load(infile)
    infile.close()
    return degrees

def printSortedDict(dictionary):
   sortedDegrees = sorted(dictionary.items(), key=lambda k: k[1][0], reverse=True)
   for degree in sortedDegrees:
       print(degree[0], "\t", degree[1][0])


main()


