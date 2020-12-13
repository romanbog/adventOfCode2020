import time

def checkEmpty(curPos, busIDList, emptyPos):
 for bus in busIDList:
  busTime = 0
  while busTime <= curPos + emptyPos:
   busTime += int(bus)
  if busTime != curPos + emptyPos:
   print("non-empty found")
   return False
 return True

def testInput(curPos, busIDList):
 currentBus = 0
 for index, bus in enumerate(busIDList):
  if bus == 'x':
   if checkEmpty(curPos, busIDList, index):
    print("Found false")
    return False
  else:
   #time.sleep(1)
   busTime = 0
   #print(bus)
   while busTime < curPos:
    busTime += int(bus)
   if(index != curPos - busTime):
    #print(curPos, busTime, index)
    return False
 return True

with open("example.txt", "r") as f: 
 array = f.read().split('\n')

arrivalTime = int(array[0])
busIDList = array[1].split(',')

curPos = 0
printCount = 0
while True:
 #print(curPos)
 if testInput(curPos, busIDList):
  break
 curPos += int(busIDList[0])
 printCount +=1 
 if printCount % 100 == 1:
  print(curPos, printCount)
 
print(curPos)

