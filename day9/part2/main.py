with open("input.txt", "r") as f: 
 array = f.read().split('\n')

position = 25
#same stuff from part1, to get our result.
while len(array) > position:
 toCompare = int(array[position])
 foundMatch = 0
 for element in array[position-25:position]:
  startSpot = array.index(element)
  for testElement in array[startSpot+1:position]:
   if int(element) + int(testElement) == toCompare:
    foundMatch = 1
    break
  if foundMatch == 1:
    break
 if foundMatch == 0:
  print(array[position])
  break
  
 position += 1
#save our result in a result integer.
result = int(array[position])
#set runningTotal to the position of array[0]
runningTotal = int(array[0])
position = 0
front = 0
back = 0
while runningTotal != result:
 #If our runningTotal is less than result, move our back +1, 
 #and add the value of that index to our runningTotal.
 if runningTotal < result:
  back += 1
  runningTotal += int(array[back])
 #Else, move our front forward one, and subtract the value that we 
 #just got rid of.
 elif runningTotal > result:
  runningTotal -= int(array[front])
  front += 1
 #If it runningTotal and result equal each other, we've found our answer!
 elif runningTotal == result:
  break

newList = []
#We have to convert our array into an int, starting from front and ending
#at back. This is so we can call min and max ^^
for element in array[front:back]:
 newList.append(int(element))

#find min and max inside of our list
smallest = min(newList)
largest = max(newList)
#Print output! :)
print(smallest + largest)
