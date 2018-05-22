"""Simple module for read and import csv files.

this module return csv elements in 2d list
"""
import csv


def readCSV(filename, delimiter=None):
    """Give file name and delimiter, it returns CSV Data.

    @Inputs:
              File Name, delimiter [optional]
    @Outputs:
              Datas From that CSV file in 2d arry:
              [[row1     of     csv]
               [row2     of     csv]
                 ...     ..     ...
               [last    row  of file]]
    """
    with open(filename, 'r') as csvFile:
        if delimiter:
            liens = csv.reader(csvFile, delimiter=delimiter)
        else:
            liens = csv.reader(csvFile)

        data = []
        for row in liens:
            data.append(row)
            # print(row)
    # data.pop()
    return data


if __name__ == '__main__':
    print("you should import this module! don't run it:)")
