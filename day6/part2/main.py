import math
from string import ascii_lowercase

with open("input.txt", "r") as f: 
 array = f.read().split('\n\n')
#print(array)
#array.pop()
#array = array[:-1]
summation = 0
summationList = []
#teams = array.split('\n')
for element in array:
 rowmax = 127
 newLine = chr(10)
 grouparray = element.split('\n')
 resultList = []
 for grpelement in grouparray:
  tempSet = set()
  for c in grpelement:
   tempSet.update(c)
  resultList.append(tempSet)
 tempFinal = set.intersection(*resultList)
 summationList.append(tempFinal)
    #if any(c in s for s in grouparray):
    
      #resultList.append(c)
 #summation += len(resultList)
 #onlyunique = ''.join(set(string))
 #trashvar = element.split('\n')
 #element = " ".join(element.splitlines())
 incrementer = 0
 for i in summationList:
  incrementer += len(i)
print(incrementer)
