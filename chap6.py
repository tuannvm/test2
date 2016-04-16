#Table printer v1
from __future__ import print_function
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    colWidths = [0] * len(table);
    for i in range(len(table)):
        for j in range(len(table[i])):
            colWidths[i] = len(max(table[i])) + 1;
    print (colWidths)


    for i in range(len(table[0])):
        for j in range(len(table)):
            print (table[j][i].rjust(colWidths[j]),end=" ")
        print()


printTable(tableData)

#tableData = ['apples', 'orangesssssss', 'cherries', 'banana']
#print (max(tableData))