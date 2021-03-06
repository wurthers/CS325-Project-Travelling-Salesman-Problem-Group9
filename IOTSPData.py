#!/usr/bin/env python
import math
import sys

class city():
    i = ""
    x = ""
    y = ""
    visited = 0

######################################
# Read from file ./inputFile.txt
######################################
def readInput(pathToInputFile):
    inputFile = open(pathToInputFile, "r")
    V = []
    with inputFile:
        for line in inputFile:
            parsedLine = map(int, line.rstrip().split())
            newCity = city()
            newCity.i = parsedLine[0]
            newCity.x = parsedLine[1]
            newCity.y = parsedLine[2]
            newCity.visited = False
            V.append(newCity)

    return V
    inputFile.close()

###################################
# Write to output File
###################################
def writeOutput(pathToInputFile, totalDistance, listOfCities, extension):
    outputFilePath = pathToInputFile + extension
    outputFile = open(outputFilePath, 'w')

    # write the total distance
    outputFile.write(str(totalDistance))
    outputFile.write("\n")

    # write the list of cities
    for city in listOfCities:
        outputFile.write(str(city.i))
        outputFile.write("\n")
    outputFile.close()
