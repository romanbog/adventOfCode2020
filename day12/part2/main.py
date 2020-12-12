with open("input.txt", "r") as f: 
 array = f.read().split('\n')

array.pop()

northSouthShipPos = 0
eastWestShipPos = 0
northSouthWayPT = 1
eastWestWayPT = 10
#shipDir = 1
#0 is north, 1 is east, 2 is south, 3 is west

for element in array:
 if element[0] == 'N':
  northSouthWayPT += int(element[1:])
 elif element[0] == 'S':
  northSouthWayPT -= int(element[1:])
 elif element[0] == 'E':
  eastWestWayPT += int(element[1:])
 elif element[0] == 'W':
  eastWestWayPT -= int(element[1:])
 elif element[0] == 'R':
  toTurn = element[1:]
  if toTurn == '90':
   tempNorthSouth = northSouthWayPT
   northSouthWayPT = -eastWestWayPT
   eastWestWayPT = tempNorthSouth
  elif toTurn == '180':
   northSouthWayPT = -northSouthWayPT 
   eastWestWayPT = -eastWestWayPT
  elif toTurn == '270':
   tempNorthSouth = northSouthWayPT
   northSouthWayPT = eastWestWayPT
   eastWestWayPT = -tempNorthSouth
 elif element[0] == 'L':
  toTurn = element[1:]
  if toTurn == '90':
   tempNorthSouth = northSouthWayPT
   northSouthWayPT = eastWestWayPT
   eastWestWayPT = -tempNorthSouth
  elif toTurn == '180':
   northSouthWayPT = -northSouthWayPT 
   eastWestWayPT = -eastWestWayPT
  elif toTurn == '270':
   tempNorthSouth = northSouthWayPT
   northSouthWayPT = -eastWestWayPT
   eastWestWayPT = tempNorthSouth

 elif element[0] == 'F':
  northSouthShipPos += northSouthWayPT * int(element[1:])
  eastWestShipPos += eastWestWayPT * int(element[1:])
'''
  if shipDir == 0:
   northSouth += int(element[1:])
  elif shipDir == 1:
   eastWest += int(element[1:])
  elif shipDir == 2:
   northSouth -= int(element[1:])
  elif shipDir == 3:
   eastWest -= int(element[1:])
'''
 #print(northSouth, eastWest, shipDir)

print(northSouthShipPos, eastWestShipPos, abs(northSouthShipPos) + abs(eastWestShipPos))
