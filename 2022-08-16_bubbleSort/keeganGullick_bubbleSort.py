# Author - Keegan Gullick
# Date - 2022-08-12
# Ticket - PVSYSENG-182
# Purpose - Practice implementation of the bubblesort algorithm


# Functions
def bubbleSortMain(inputList):
    # Loops over the list
    for ii in range (0, len(inputList)):
        # Loop over pairs
        for jj in range(0, (len(inputList) - ii - 1)):
            # Compare and swap if not in the correct order
            if inpustList[jj] > inputList[jj + 1]:
                inputList[jj], inputList[jj + 1] = inputList[jj + 1], inputList[jj]


# Gets data from the user
inData = [int(x) for x in input("Space separated integers: ")].split()]


# Bubble Sort
bubbleSortMain(inData)


# Results
print(inData)