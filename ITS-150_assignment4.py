
### Located in the same directory and inport it's data.
### This file has city name, state, population in 2000, 
### and population in 2010. It will calculate the percentage 
### of growth between 2000 and 2010 and create a file named 
### LeastGrowth.txt that contains the top five for lowest growth
### the city name, percentage of growth, and is ordered by growth. 


def main():
    citiesList = makeFileList("Cities.txt") # pass filename to function and get usable list back
    popPercentList = makePopPercentList(citiesList) # send citiesList to func and get growthList back
    popPercentList.sort(key=lambda line: line[1]) # sort popPercentList by growth percentage
    writeOutputFile(popPercentList) # send pop list to output func

# open filname from main() and turn it into a usable list with each line of data
# placed in a seperate list, and each item in the list made a sepearate item. 
# Will also make the poplation data an int or float so it can be used for calculations.
def makeFileList(filename):
    infile = open(filename, 'r', encoding='utf-8-sig')
    list = [line.rstrip() for line in infile] # strip \n off from the right side
    infile.close()
    for i in range(len(list)):
        list[i] = list[i].split(',') # break up a long string into individual data at the commas.
        list[i][2] = eval(list[i][2]) # population in 2000. Make it a usable number not string. 
        list[i][3] = eval(list[i][3]) # population in 2010. Make it a usable number not string. 
    return list

# Get cities list from main() and calculate population growth.
# Create new growthList with city name and growth percentage and return it to main().
def makePopPercentList(cities):
    growthList = [] # create growthList
    for i in range(len(cities)):
        x = [] # create list x
        growth = ((cities[i][3]) - (cities[i][2])) / (cities[i][2]) * 100 # calc percentage. (2010-2000/2000)*100
        x.append(cities[i][0]) # add city name list x
        x.append(growth) # add growth percentage to list x
        growthList.append(x) # add list x to growthList
    return growthList 

# get popList from main(), change it to a string and write it to a txt file.
def writeOutputFile(popList):
    outfile = open("LeastGrowth.txt", 'w') # open or create output txt file.
    for i in range(5): # take top 5 lowest percentages
        outfile.write(popList[i][0] + ',' + str(round(popList[i][1], 1)) +  "\n") # create string values of city name and growth and add \n
    outfile.close() #  close output file


main()