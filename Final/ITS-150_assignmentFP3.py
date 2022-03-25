from fileinput import filename
import pickle

def main():
    fileName = "DegreesDict.dat"
    dictionary = getDictionary(fileName)
    print(dictionary)

def getDictionary(fileName):
    infile = open(fileName, 'rb')
    degrees = pickle.load(infile)
    infile.close()
    return degrees



main()