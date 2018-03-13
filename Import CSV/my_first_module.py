import csv

def getInput(fileName):
  with open(fileName) as f:
    my_reader = csv.reader(f)
    data=[]
    for row in my_reader:
      data.append(row)
    return data