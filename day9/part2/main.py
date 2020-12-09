with open("input.txt", "r") as f: 
 array = f.read().split('\n')

position = 25
while len(array) > position:
 toCompare = int(array[position])
 foundMatch = 0
 #print(array[:position])
 #print("searching for " + array[position])
 for element in array[position-25:position]:
  startSpot = array.index(element)
  for testElement in array[startSpot+1:position]:
   #print("Adding :" + element + "+" + testElement)
   if int(element) + int(testElement) == toCompare:
    #print("Found!")
    foundMatch = 1
    break
  if foundMatch == 1:
    break
 if foundMatch == 0:
  print(array[position])
  break
 #print(array[:position])
  
 position += 1
 #if foundMatch == 0:
  #print array[position]
  #break
result = int(array[position])
runningTotal = int(array[0])
position = 0
front = 0
back = 0
while runningTotal != result:
 #print(runningTotal, result)
 if runningTotal < result:
  back += 1
  runningTotal += int(array[back])
 elif runningTotal > result:
  runningTotal -= int(array[front])
  front += 1
 elif runningTotal == result:
  print(front + back)
  break

newList = []
for element in array[front:back]:
 newList.append(int(element))

smallest = min(newList)
largest = max(newList)
print(smallest + largest)
#print(int(array[front]) + int(array[back]))
