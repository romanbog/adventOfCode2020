from collections import defaultdict

def search(searchTerm, ruleDict, bagResult):
 if(searchTerm not in ruleDict):
  return
 #print(searchTerm)
 #bagResult.add(searchTerm)
 setInside = ruleDict[searchTerm]
 for element in setInside:
  bagResult.add(element)
  search(element, ruleDict, bagResult)
 
 
with open("input.txt", "r") as f: 
 array = f.read().split('\n')

summation = 0
#sets every value to an empty set
ruleDict = defaultdict(set)
#for every group
array.pop()
print(array)
for rule in array:
 #replace newlines
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
  ruleDict[string[i+1] + ' ' + string[i+2]].add(bagName)
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
search(searchTerm, ruleDict, bagResult)
#print(ruleDict)
print(len(bagResult))
#if searchTerm in ruleDict:
 #print("hi")
 #print(search(searchTerm, ruleDict))
 #print(search(searchTerm, ruleDict)

