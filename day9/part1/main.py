with open("input.txt", "r") as f: 
 array = f.read().split('\n')

#first 25 are preamble, so we'll start there. 
position = 25
#remove last position, it's a whitespace for some reason
array.pop()
#while we're in our array
while len(array) > position:
 toCompare = int(array[position])
 foundMatch = 0
 #For every element from position to pos-25:
 for element in array[position-25:position]:
  startSpot = array.index(element)
  #for every element in position to pos-25
  for testElement in array[startSpot+1:position]:
   #add together our two elements
   if int(element) + int(testElement) == toCompare:
    #if we find a match, we good
    foundMatch = 1
    break
  if foundMatch == 1:
  #match found, we don't have to look through the rest of our values.
    break
 if foundMatch == 0:
  #if we don't find a match, print and quit.
  print(array[position])
  quit()
  
 position += 1
