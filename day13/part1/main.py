with open("input.txt", "r") as f: 
 array = f.read().split('\n')

arrivalTime = int(array[0])
busIDList = array[1].split(',')

fastestPos = 100000000000000
bestBus = 0

for bus in busIDList: 
 if bus == 'x':
  pass
 else:
  currentPos = 0
  print(bus)
  while currentPos <= arrivalTime:
   currentPos += int(bus)
  if currentPos < fastestPos:
   fastestPos = currentPos
   bestBus = int(bus)
  print(fastestPos)

timeToWait = fastestPos - arrivalTime
print(timeToWait, bestBus, timeToWait * bestBus)
#print(timeToWait)
'''
currentLoc = arrivalTime
while bestBus == 0:
 for bus in busIDList:
  print(bus, currentLoc)
  if bus == 'x':
   pass
  elif int(bus) % arrivalTime == 0:
   #print(int(bus & arrivalTime))
   bestBus = bus
 currentLoc += 1
'''
#print(bus, currentLoc)
