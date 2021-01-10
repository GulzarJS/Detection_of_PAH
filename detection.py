# Created by Gulzar Safar on 03/01/2021

import pickle
import numpy as np


# Function to create integer list with max value
def createList(maxNumber):
    newlist = []
    for i in range(1, int(maxNumber)):
        newlist.append(i)
    return newlist


# Function to convert string list to float list
def convertStringListToFloatList(stringList):
    floatList = []
    for i in stringList:
        floatList.append(float(i))
    return floatList


# Function to find lifetime of molecule
def findLifetime(f, t, A):
    # x = - t / lifetime
    # f = 1 * exp(x)
    x = np.log(f/A)
    if x != 0:
        lifetime = - t / x
        lifetime *= 1000000000
    else:
        lifetime = 0
    return lifetime.__round__(1)


# Function to get molecule name with its lifetime
def getMoleculeName(listLifetime, dictMolecule):
    moleculeNames = []
    for i in listLifetime:
        moleculeNames.append(dictMolecule[i])
    return moleculeNames


# Function to get concentration of molecules
# proportion(concentration) = allConcentrations / nbOfTheSameMoleculeInMeasurement
def getProportion(dictLifetime, dictConcentration):
    listProportion = []

    for i in dictLifetime:
        listProportion.append((dictConcentration[i]/dictLifetime[i]).__round__(1))

    return listProportion


# Function to define that which molecules is in mixtures
def getMolecules(mixture, dictMolecule):
    listLifetime = list(dictMolecule.keys()) # list which contains all lifetime numbers
    dictLifetime = {} # dictionary to hold lifetimes of molecules and their numbers which are in mixtures
    dictConcentration = {} # dictionary to hold lifetimes of molecules and their sum of concentrations which are in mixtures
    moleculeNames = []
    proportions = []

    t_step = 0.0000000001
    A = createList(max(convertStringListToFloatList(mixture))) # possible numbers of concentrations

    for i in range(0, len(mixture)):
        for l in A:
            if findLifetime(mixture[i], (i + 1) * t_step, l) in listLifetime:
                if findLifetime(mixture[i], (i + 1) * t_step, l) not in dictConcentration:
                    dictConcentration[findLifetime(mixture[i], (i + 1) * t_step, l)] = l
                else:
                    dictConcentration[findLifetime(mixture[i], (i + 1) * t_step, l)] += l

                if findLifetime(mixture[i], (i + 1) * t_step, l) not in dictLifetime:
                    dictLifetime[findLifetime(mixture[i], (i + 1) * t_step, l)] = 1
                else:
                    dictLifetime[findLifetime(mixture[i], (i + 1) * t_step, l)] += 1
            else:
                continue

    moleculeNames = getMoleculeName(list(dictLifetime.keys()), dictMolecule)
    proportions = getProportion(dictLifetime, dictConcentration)
    return moleculeNames, proportions


# Main function which we analyse mixtures
def main():

    # Reading all mixture files, converting them to Float list

    # reading mixture 1
    infile = open("mixture1.dat", 'rb')
    mixture1 = pickle.load(infile, encoding='bytes')
    mixture1 = (convertStringListToFloatList(mixture1))
    infile.close()
    # reading mixture 2
    infile = open("mixture2.dat", 'rb')
    mixture2 = pickle.load(infile, encoding='bytes')
    mixture2 = (convertStringListToFloatList(mixture2))
    infile.close()
    # reading mixture 3
    infile = open("mixture3.dat", 'rb')
    mixture3 = pickle.load(infile, encoding='bytes')
    mixture3 = (convertStringListToFloatList(mixture3))
    infile.close()
    # reading mixture 4
    infile = open("mixture4.dat", 'rb')
    mixture4 = pickle.load(infile, encoding='bytes')
    mixture4 = (convertStringListToFloatList(mixture4))
    infile.close()

    # Initialising dictionary which holds Molecules and their lifetimes
    dictMolecule = {5.8: "Anthracene", 8.9: "Benzofluoranthene", 38.6: "Benzopyrène", 57.8: "Chrysene",
                    200.9: "Naphtalene", 516.2: "Pyrene"}

    # Analysing mixtures

    mixture1_result = getMolecules(mixture1, dictMolecule)
    mixture2_result = getMolecules(mixture2, dictMolecule)
    mixture3_result = getMolecules(mixture3, dictMolecule)
    mixture4_result = getMolecules(mixture4, dictMolecule)

    print("===============================================================================================================")
    print("There are melecules ", mixture1_result[0], " with proportion ", mixture1_result[1], " in mixture 1")
    print("===============================================================================================================")
    print("There are melecules ", mixture2_result[0], " with proportion ", mixture2_result[1], " in mixture 2")
    print("===============================================================================================================")
    print("There are melecules ", mixture3_result[0], " with proportion ", mixture3_result[1], " in mixture 3")
    print("===============================================================================================================")
    print("There are melecules ", mixture4_result[0], " with proportion ", mixture4_result[1], " in mixture 4")
    print("===============================================================================================================")






main()