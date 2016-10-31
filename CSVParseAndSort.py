import csv as csv

pulledRows = []
csvFile = csv.reader(open("csvSample.csv", 'rt', encoding="latin1"))
rows = list(csvFile)

# Sorts pulledRows in ascending order by date and returns a string
# containing the ordered values from the words column


def generatePhrase(pulledRows):
    selectRows(rows)
    resultPhrase = " "

    # Insertion sorts list of rows from .csv by values in start date column
    for x in range(1, len(pulledRows)):
        currentRow = pulledRows[x][:]
        position = x
        while(position > 0 and int(pulledRows[position - 1][13]) > int(currentRow[13])):
            pulledRows[position] = pulledRows[position - 1][:]
            position = position - 1
        pulledRows[position] = currentRow

    for x in range(0, len(pulledRows)):
        resultPhrase += (pulledRows[x][16] + " ")

    return resultPhrase


# Parse .csv file and generate list of valid rows
def selectRows(rows):

    for x in range(1, len(rows)):
        if(checkDate(rows[x]) == True):
            pulledRows.append(rows[x])


# Compare dates while parsing to date: 09/06/2010
def checkDate(currentRow):

    compareDate = 1283731200  # 09/06/2010 in Unix time
    isGood = False

    if((compareDate - int(currentRow[13])) > 0):
        isGood = True

    return isGood


print(generatePhrase(pulledRows))
