from collections import defaultdict

def search(searchTerm, ruleDict, bagResult):
 #if(searchTerm not in ruleDict):
  #return 0
 #print(searchTerm)
 #bagResult.add(searchTerm)
 summation = 0
 setInside = ruleDict[searchTerm]
 #print(setInside)
 for element in setInside:
  print(element)
  elementArray = element.split()
  #print(elementArray)
  #print(elementArray[2])
  #bagResult.add(element)
  #summation += int(elementArray[2])
  summation += int(elementArray[2])
  #print(''.join(elementArray[1:]))
  summation *= int(elementArray[2]) * search(''.join(elementArray[1:]), ruleDict, bagResult)
 return summation
 
 
with open("example.txt", "r") as f: 
 array = f.read().split('\n')

#sets every value to an empty set
ruleDict = defaultdict(set)
#for every group
array.pop()
#print(array)
for rule in array:
 #replace newlines
 print(rule)
 string = rule.split()
 #bagName = " "
 #string[:2] = [bagName]
 bagName = string[0]
 bagName += " "
 bagName += string[1]
 #bagName = string[:1]
 #bagName = ' '.join(string[1])
 #print(bagName)
 counter = 5
 toAdd = ""
 #print(string)
 #print(rule)
 for i in range(4, len(string), 4):
  ruleDict[string[i+1] + ' ' + string[i+2]].add(bagName + ' ' + string[i])
  #print(ruleDict)
'''
 while(counter + 1 <= len(string)):
  toAdd += string[counter]
  toAdd += " "
  toAdd += string[counter + 1]
  counter += 2
  #toAdd += " "
  #print(toAdd)
  #toAdd += string[counter + 1]
  #print(toAdd)
  
  #ruleDict.update({bagName : toAdd})
  
  #ruleDict.update({toAdd : bagName})
  ruleDict[toAdd].add(bagName)
  toAdd = ""
  counter += 2
'''
#print(ruleDict)
searchTerm = 'shiny gold'
#print(ruleDict[searchTerm])
bagResult = set()
print(search(searchTerm, ruleDict, bagResult))
print(ruleDict)
print(len(bagResult))
#if searchTerm in ruleDict:
 #print("hi")
 #print(search(searchTerm, ruleDict))
 #print(search(searchTerm, ruleDict)

