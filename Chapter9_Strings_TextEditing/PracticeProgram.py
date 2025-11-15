''' For practice, write a function named printTable() that takes a list of lists of
strings and displays it in a well-organized table with each column right-justified.
Assume that all the inner lists will contain the same number of strings.
For example, the value could look like this'''

tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

def printTable(tableData):
    Welcome_message = ' Welcome to my Python Row Column creator, Written by Marshal Olimmah '
    Welcome_message = Welcome_message.center(100, '*')
    print(Welcome_message)

## Get the number of colums to use
    colwidths = [0]* len(tableData)

     # Find the longest word in each column
    for i in range(len(tableData)):
        colwidths[i] = max(len(item) for item in tableData[i])

      # Print the table row by row
    numRows = len(tableData[0])
    for row in range(numRows):
        rowItems = []
        for col in range(len(tableData)):
            rowItems.append(tableData[col][row].rjust(colwidths[col]))
        print(" ".join(rowItems))
