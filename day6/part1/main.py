import math

with open("input.txt", "r") as f: 
 array = f.read().split('\n\n')
#print(array)
#array.pop()
#array = array[:-1]
summation = 0
for element in array:
 rowmax = 127
 newLine = chr(10)
 string = element.replace("\n", "" )
 onlyunique = ''.join(set(string))
 print(string)
 print(len(onlyunique))
 summation += len(onlyunique)
 #trashvar = element.split('\n')
 #element = " ".join(element.splitlines())
#print(array)
print(summation)
