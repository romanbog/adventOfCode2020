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
 #print(array[:position])
  
 position += 1
 #if foundMatch == 0:
  #print array[position]
  #break
