# Program 3
# The file “DegreesDict.dat” stores a dictionary where each field of study is a key and
# each value is a two-tuple of the form (ex. number of degrees in 1981, number of degrees in 2010).

# Write a well-documented (commented) program that reads data from the file “DegreesDict.dat” and 
# then displays a histogram, in descending order of the number of degrees conferred in 1981.

# The output of the program should be as follows.

# Business ******************** 200,521
# Education *********** 108,074
# Social sciences and history **********  100,513
# Engineering ****** 63,642
# Computer and info. science ** 15,121
####################################################################################################

# import pickle for working with binary files
import pickle
# main() func will set filename, get dictionary from .dat file and print a sorted dictionary.
def main():
    fileName = "DegreesDict.dat"
    dictionary = getDictionary(fileName)
    print()
    printSortedDict(dictionary)
    print()

def getDictionary(fileName):
    infile = open(fileName, 'rb') # set infile to read binary for the filename that is passed in
    degrees = pickle.load(infile) # load dictionary from file and set degrees variable
    infile.close() # close infile connection
    return degrees # return dictionary

def printSortedDict(dictionary):
    sortedDegrees = sorted(dictionary.items(), key=lambda k: k[1][0], reverse=True) # sort dictionary degrees in 1981 using lambda function
    for degree in sortedDegrees: # for each degree in sorted dict, print degree name, histogram, and amount of degrees
        print(degree[0], histogram(degree[1][0]), degree[1][0])


def histogram(input): # will pass in number of degrees when function is called
    starCount = round(input / 10000) # divide input by 10000 and set star count
    return "*" * starCount # return the string of stars matching the star count


main()



