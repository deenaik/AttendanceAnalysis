import csv
import os

def fileImportcsv(inputFile):
    empFile = open(inputFile)
    empReader = csv.reader(empFile)
    empData = list(empReader)
    # print empData
    return empData, inputFile

def emp_records(empData, inputFile):
    empRecord = []
    rowLength = 0
    for e in empData:
        if e[1] != '':
            colDate = 8
            if e[1] != 'Name of the Employee':
                while colDate <= len(empData[0]) - 1:
                    empRecord.extend([[inputFile[:5],empData[0][colDate],empData[rowLength][1],empData[rowLength][colDate],empData[rowLength + 1][colDate]]])
                    colDate = colDate + 1
        rowLength = rowLength + 1    
    return empRecord

def fileExportcsv(outputFile, outputRecords):
    with open(outputFile, 'ab') as fp:
        a = csv.writer(fp, delimiter = ',')
        a.writerows(outputRecords)
        
def mainRun(outputFile):
    for e in os.listdir('.'):
        if e.endswith('.csv'):
            fileExportcsv(outputFile, emp_records(fileImportcsv(e)[0],fileImportcsv(e)[1]))
        
mainRun('bak/test_jan-apr-16.csv')