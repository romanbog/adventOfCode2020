with open("input.txt", "r") as f: 
 array = f.read().split('\n')

array.pop()

#set up initial ship and waypoint position
northSouthShipPos = 0
eastWestShipPos = 0
northSouthWayPT = 1
eastWestWayPT = 10

for element in array:
#move our waypoint NSEW:
 if element[0] == 'N':
  northSouthWayPT += int(element[1:])
 elif element[0] == 'S':
  northSouthWayPT -= int(element[1:])
 elif element[0] == 'E':
  eastWestWayPT += int(element[1:])
 elif element[0] == 'W':
  eastWestWayPT -= int(element[1:])
#rotate waypoint right. I had to do some math for this one! 
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
#rotate waypoint left. Right, but inverted.
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
#Move our ship forward to our waypoint.
 elif element[0] == 'F':
  northSouthShipPos += northSouthWayPT * int(element[1:])
  eastWestShipPos += eastWestWayPT * int(element[1:])

#Print final position of ship and manhattan distance.
print(northSouthShipPos, eastWestShipPos, abs(northSouthShipPos) + abs(eastWestShipPos))
