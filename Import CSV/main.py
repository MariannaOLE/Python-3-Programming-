from my_first_module import *
def processData(rawData):
  processData = []
  #add the header
  header = rawData[0].copy()
  header.append('diff')
  processData.append(header)

  firstRow = rawData[1].copy()
  firstRow.append('NA')
  processData.append(firstRow)
  
  for i in range(2, len(rawData)):
    currentPrice = float(rawData[i][1])
    previousPrice = float(rawData[i-1] [1])
    diff = currentPrice - previousPrice
    processData.append([rawData[1][0], rawData[i][1], diff])
  return processData
  
def doWork(fileName='data_csv.csv'):
  input = getInput(fileName)
  data = processData(input)
  print(data)
 
doWork()
  
  
  
  
  
  
  