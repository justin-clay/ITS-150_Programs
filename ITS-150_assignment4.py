


def main():
    citiesList = makeFileList("Cities.txt")
    popPercentList = makePopPercentList(citiesList)
    popPercentList.sort(key=lambda line: line[1])
    writeOutputFile(popPercentList)

def makeFileList(filename):
    infile = open(filename, 'r', encoding='utf-8-sig')
    list = [line.rstrip() for line in infile]
    infile.close()
    for i in range(len(list)):
        list[i] = list[i].split(',')
        list[i][2] = eval(list[i][2]) # population in 2000
        list[i][3] = eval(list[i][3]) # population in 2010
    return list

def makePopPercentList(cities):
    growthList = []
    for i in range(len(cities)):
        x = []
        growth = ((cities[i][3]) - (cities[i][2])) / (cities[i][2]) * 100
        x.append(cities[i][0]) 
        x.append(growth)
        growthList.append(x)
    return growthList


def writeOutputFile(popList):
    outfile = open("LeastGrowth.txt", 'w')
    for i in range(5):
        outfile.write(popList[i][0] + ',' + str(round(popList[i][1], 1)) +  "\n")
    outfile.close()


main()