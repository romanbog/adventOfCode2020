def search(searchTerm, ruleDict):
 if searchTerm in ruleDict:
  for element in ruleDict:
   summation = 0
   summation += recursiveSearch(searchTerm, ruleDict, element)
 return summation
 
def recursiveSearch(searchTerm, ruleDict, currElem):
 values = ruleDict.get(currElem)
 print(values)
 print(currElem)
 return 1

with open("input.txt", "r") as f: 
 array = f.read().split('\n')

summation = 0
ruleDict = {}
#for every group
array.pop()
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
 toAdd = " "
 #print(string)
 while(counter + 1 <= len(string)):
  toAdd += string[counter]
  toAdd += " "
  toAdd += string[counter + 1]
  counter += 2
  #toAdd += " "
  #print(toAdd)
  #toAdd += string[counter + 1]
  #print(toAdd)
  
  ruleDict.update({bagName : toAdd})
  toAdd = " "
  counter += 2

searchTerm = 'shiny gold'
if searchTerm in ruleDict:
 print("hi")
 print(search(searchTerm, ruleDict))
 #print(search(searchTerm, ruleDict)

