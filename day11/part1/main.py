#for element in array:
 #newElement = list(element)
 #newArray.append(newElement)
 #newArray[array.index(element)] = list(element)
#newArray = [[]]
#print(newArray)

def placeSeats(array):
 elementNum = 0
 for element in array:
  newElement = ''
  #row = list(element)
  seatNum = 0
  for seat in element:
   #find occupied seats
   occupied = 0
   #Current problem: change to make it so that indexes work. str.index(stuff)
   #print(element.index(seat))
   #print(seatNum)
   try:
    #print(array[array.index(element)+1][seatNum-1])
    #print(array[array.index(element)+1][seatNum])
    #print(array[elementNum+1][seatNum])
    #if array[array.index(element)+1][seatNum+1] == '#':
    if elementNum <= len(array) and seatNum+1 <= len(element) and  array[elementNum+1][seatNum+1] == '#':
     #print("found: ", elementNum+1, seatNum+1)
     #print(array[elementNum+1][seatNum+1], elementNum+1, seatNum+1)
     #print(seat)
    #if array[array.index(element)+1][element.index(seat-1):element.index(seat)] == '#':
     occupied += 1
     #print(array.index(element), array.index(seat))
   except:
    pass
   try:
    #if array[array.index(element)+1][element.index(seat)] == '#':
    #if array[array.index(element)+1][seatNum] == '#':
    if elementNum+1 <= len(array) and array[elementNum+1][seatNum] == '#':
     #print("found: ", elementNum+1, seatNum)
     occupied += 1
   except:
    pass
   try:
    #if array[array.index(element)+1][element.index(seat)+1] == '#':
    #if array[array.index(element)+1][seatNum-1] == '#':
    if elementNum+1 <= len(array) and seatNum > 0 and array[elementNum+1][seatNum-1] == '#':
     #print("found: ", elementNum+1, seatNum-1)
     occupied += 1
   except:
    pass
   try:
    #if array[array.index(element)][element.index(seat)-1] == '#':
    #if array[array.index(element)][seatNum+1] == '#':
    if seatNum+1 <= len(element) and  array[elementNum][seatNum+1] == '#':
     #print("found: ", elementNum, seatNum+1)
     occupied += 1
   except:
    pass

   #try:
    #if array[array.index(element)][element.index(seat)] == '#':
     #occupied += 1
   #except:
    #pass

   try:
    #if array[array.index(element)][element.index(seat)+1] == '#':
    #if array[array.index(element)][seatNum-1] == '#':
    if seatNum > 0 and array[elementNum][seatNum-1] == '#':
     #print("found: ", elementNum, seatNum-1)
     occupied += 1
   except:
    pass
   try:
    #if array[array.index(element)-1][element.index(seat)-1] == '#':
    #if array[array.index(element)-1][seatNum-1] == '#':
    if elementNum > 0 and array[elementNum-1][seatNum] == '#':
     #print("found: ", elementNum-1, seatNum)
     occupied += 1
   except:
    pass
   try:
    #if array[array.index(element)-1][element.index(seat)] == '#':
    #if array[array.index(element)-1][seatNum] == '#':
    if elementNum > 0 and seatNum+1 <= len(element) and array[elementNum-1][seatNum+1] == '#':
     #print("found: ", elementNum-1, seatNum+1)
     occupied += 1
   except:
    pass
   try:
    #if array[array.index(element)-1][element.index(seat)+1] == '#':
    #if array[array.index(element)-1][seatNum+1] == '#':
    if elementNum > 0 and seatNum > 0 and array[elementNum-1][seatNum-1] == '#':
     #print("found: ", elementNum-1, seatNum-1)
     occupied += 1
   except:
    pass
   #print(elementNum)
   if seat == 'L' and occupied == 0:
    #print(occupied)
    newElement += '#'
   elif seat == '#' and occupied >= 4:
    #print('turned')
   #newArray[array.index(element)][element.index(seat)] = 'L'
   #seat = 'L' + seat[1:]
   #seat = seat.replace('#', 'L')
    newElement += 'L'
   else:
    newElement += seat
   seatNum += 1
   #print(seat, occupied, elementNum, seatNum)
  #else:
   #newArray[array.index(element)][element.index(seat)] = [array.index(element)][element.index(seat)]
  elementNum += 1
  newArray.append(newElement)
 return newArray
   

with open("input.txt", "r") as f: 
 array = f.read().split('\n')

#with open("input.txt", "r") as f:
 #testArray = f.readlines()

#print(testArray)
#array.pop()

#print(array[0])
#print(list(array[0]))
#for result in map(list, array):
 #pass

newArray = []
#newArray = placeSeats(array)
#print("through alg once")
#print(newArray)
#array = newArray
#print("array set to new")
#print(array)
#newArray = []
#newArray = placeSeats(array)
#print("through alg twice")
#print(newArray)
#array = newArray
#newArray = []
#newArray = placeSeats(array)
#print(newArray)
#newArray = placeSeats(array)

while newArray != array:
 #array = newArray
 #newArray = []
 newArray = placeSeats(array)
 if newArray == array:
  break
 else:
  array = newArray
  newArray = []

occupiedSeats = 0
for element in array:
 for char in element:
  if char == '#':
   occupiedSeats += 1

print(newArray)
print(occupiedSeats)
#print(newArray)
#print(array)

