import sys
import os
sys.path.append(os.path.abspath('..'))
from readcsvdataset import readCSV

iris = readCSV('iris.csv', ',')
for i in iris:
    print(i)
