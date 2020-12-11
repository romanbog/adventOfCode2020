#for element in array:
 #newElement = list(element)
 #newArray.append(newElement)
 #newArray[array.index(element)] = list(element)
#newArray = [[]]
#print(newArray)

def placeSeats(array):
 for element in array:
  newElement = ''
  #row = list(element)
  for seat in element:
   #find occupied seats
   occupied = 0
   #Current problem: change to make it so that indexes work. str.index(stuff)
   try:
    if array[array.index(element)+1][element.index(seat)-1] == '#':
     occupied += 1
   except:
    pass
   try:
    if array[array.index(element)+1][element.index(seat)] == '#':
     occupied += 1
   except:
    pass
   try:
    if array[array.index(element)+1][element.index(seat)+1] == '#':
     occupied += 1
   except:
    pass
   try:
    if array[array.index(element)][element.index(seat)-1] == '#':
     occupied += 1
   except:
    pass
   try:
    if array[array.index(element)][element.index(seat)] == '#':
     occupied += 1
   except:
    pass
   try:
    if array[array.index(element)][element.index(seat)+1] == '#':
     occupied += 1
   except:
    pass
   try:
    if array[array.index(element)-1][element.index(seat)-1] == '#':
     occupied += 1
   except:
    pass
   try:
    if array[array.index(element)-1][element.index(seat)] == '#':
     occupied += 1
   except:
    pass
   try:
    if array[array.index(element)-1][element.index(seat)+1] == '#':
     occupied += 1
   except:
    pass
   if seat == 'L' and occupied == 0:
    #print(occupied)
    newElement += '#'
   elif seat == '#' and occupied >= 4:
    print(occupied)
   #newArray[array.index(element)][element.index(seat)] = 'L'
   #seat = 'L' + seat[1:]
   #seat = seat.replace('#', 'L')
    newElement += 'L'
   else:
    newElement += seat
  #else:
   #newArray[array.index(element)][element.index(seat)] = [array.index(element)][element.index(seat)]
  newArray.append(newElement)
 return newArray
   

with open("input.txt", "r") as f: 
 array = f.read().split('\n')

#with open("input.txt", "r") as f:
 #testArray = f.readlines()

#print(testArray)
array.pop()

#print(array[0])
#print(list(array[0]))
#for result in map(list, array):
 #pass

newArray = []
newArray = placeSeats(array)
print("through alg once")
print(newArray)
array = newArray
print("array set to new")
print(array)
newArray = []
newArray = placeSeats(array)
print("through alg twice")
print(newArray)
'''
while newArray != array:
 newArray = placeSeats(array)
 if(newArray == array):
  break
 else:
  array = newArray
  newArray = []
'''
empties = 0
for element in newArray:
 for char in element:
  if char == '#':
   empties += 1
'''
print(newArray)
print(empties)
#print(newArray)
print(array)
'''
