import math

with open("input.txt", "r") as f: 
 array = f.read().split('\n\n')

#summation = 0
summationList = []

#for every group
for element in array:
 #split group into array of people (on newline)
 grouparray = element.split('\n')
 resultList = []
 #for every person
 for grpelement in grouparray:
  tempSet = set()
  #for all char c in a person, add it to our new set
  for c in grpelement:
   tempSet.update(c)
  #add our set of chars into an array
  resultList.append(tempSet)
 #intersection of resultList will give us all unique chars that are 
 #found inside every element of resultList
 setOfUnique = set.intersection(*resultList)
 #We'll add of those unique chars into a list, so every element is a group.
 summationList.append(setOfUnique)
 incrementer = 0
 #now, we count up all the stuff inside of our list of unique chars
 for i in summationList:
  incrementer += len(i)
#poggers :0
print(incrementer)
