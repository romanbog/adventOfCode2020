import collections
import itertools

def recursiveFind(joltList, adapter, solutionDictionary):
 position = 0
 if joltList[position] == adapter:
  return 1
 if joltList[position] in solutionDictionary.keys():
  return solutiondictionary[joltList[position]]
 sumOfNexts = 0
 #while position < len(joltList):
 #print(joltList)
 if joltList[1] == joltList[0] + 1:
  #solutionDictionary[joltList[position] = 
  sumOfNexts += recursiveFind(joltList[1:], adapter, solutionDictionary)
 elif joltList[1] == joltList[0] + 2:
  sumOfNexts += recursiveFind(joltList[1:], adapter, solutionDictionary)
 elif joltList[1] == joltList[0] + 3:
  sumOfNexts += recursiveFind(joltList[1:], adapter, solutionDictionary)
 try:
  if joltList[2] in joltList:
   if joltList[2] == joltList[0] + 2:
    sumOfNexts += recursiveFind(joltList[2:], adapter, solutionDictionary)
   elif joltList[2] == joltList[0] + 3:
    sumOfNexts += recursiveFind(joltList[2:], adapter, solutionDictionary)
 except IndexError:
  pass
 try:
  if joltList[3] in joltList:
   if joltList[3] == joltList[0] + 3:
    sumOfNexts += recursiveFind(joltList[3:], adapter, solutionDictionary)
 except IndexError:
  pass
 return sumOfNexts
'''
 elif joltList[1] == joltList[0] + 3:
  sumOfNexts += recursiveFind(joltList[1:], adapter)
 elif joltList[2] == joltList[0] + 3:
  sumOfNexts += recursiveFind(joltList[2:], adapter)
 elif joltList[3] == joltList[0] + 3:
  sumOfNexts += recursiveFind(joltList[3:], adapter)
'''

with open("input.txt", "r") as f: 
 array = f.read().split('\n')

joltList = []
array.pop()
for element in array:
 joltList.append(int(element))

deviceAdapter = max(joltList) + 3
joltList.append(deviceAdapter)
joltList.append(0)
joltList.sort()
oneDifference = 0
twoDifference = 0 
threeDifference = 0

solutionDictionary = {}
#print(recursiveFind(joltList, deviceAdapter, solutionDictionary))
permutations = []
permPos = 0
position = 1
lastNum = 0
tempList = [0]
while position < len(joltList):
 if joltList[position - 1] == joltList[position] - 1:
  tempList.append(joltList[position])
 else:
  permutations.append(tempList)
  tempList = []
  tempList.append(joltList[position])
 position += 1

total = 1
for element in permutations:
 if(len(element) == 5):
  total *= 7
 elif(len(element) == 4):
  total *= 4
 elif(len(element) == 3):
  total *= 2
 elif len(element) == 2 or len(element) == 1:
  pass
 #print(len(element))
 #total *= len(element)
#when 5, mult 7
#when 4, mult 4
#when 3, mult 2
#when 2 or 1, mult 1
print(permutations)
print(total)
#print(itertools.combinations[joltList[-1]])

'''
print(oneDifference)
print(twoDifference)
print(threeDifference)
print(oneDifference * threeDifference)
'''
