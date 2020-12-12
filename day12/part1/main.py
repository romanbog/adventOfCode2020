with open("input.txt", "r") as f: 
 array = f.read().split('\n')

array.pop()

northSouth = 0
eastWest = 0
shipDir = 1
#0 is north, 1 is east, 2 is south, 3 is west

for element in array:
 if element[0] == 'N':
  northSouth += int(element[1:])
 elif element[0] == 'S':
  northSouth -= int(element[1:])
 elif element[0] == 'E':
  eastWest += int(element[1:])
 elif element[0] == 'W':
  eastWest -= int(element[1:])
 elif element[0] == 'R':
  toTurn = element[1:]
  if toTurn == '90':
   shipDir += 1
  elif toTurn == '180':
   shipDir += 2
  elif toTurn == '270':
   shipDir += 3
  if shipDir > 3:
   shipDir = shipDir - 4
 elif element[0] == 'L':
  toTurn = element[1:]
  if toTurn == '90':
   shipDir -= 1
  elif toTurn == '180':
   shipDir -= 2
  elif toTurn == '270':
   shipDir -= 3
  if shipDir < 0:
   shipDir = shipDir + 4
 elif element[0] == 'F':
  if shipDir == 0:
   northSouth += int(element[1:])
  elif shipDir == 1:
   eastWest += int(element[1:])
  elif shipDir == 2:
   northSouth -= int(element[1:])
  elif shipDir == 3:
   eastWest -= int(element[1:])
 #print(northSouth, eastWest, shipDir)

print(northSouth, eastWest, abs(northSouth) + abs(eastWest))
