# Write your code here :-)
tableData = [
    ['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']
]

def printTable(tableData):
    # Determine Max Width of Each Column

    numCols = len(tableData[0])
    numRows = len(tableData)

    numRows

    # Compute column widths by scanning column-wise
    colWidths = [0] * numCols
    for col in range(numCols):
        colMax = 0
        for row in range(numRows):
            colMax = max(colMax, len(tableData[row][col]))
        colWidths[col] = colMax


    # Print table row by row (normal orientation)
    for row in range(numRows):
        rowItems = [tableData[row][col].rjust(colWidths[col])
            for col in range(numCols)
        ]
        print(" ".join(rowItems))
