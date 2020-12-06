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
 #intersection of resultList will give us all chars that are 
 #found inside every element of resultList
 setOfUnique = set.intersection(*resultList)
 #We'll all of those unique chars into a list, sectioned by groups.
 summationList.append(setOfUnique)
 incrementer = 0
 #now, we count up all the stuff inside of our list of unique chars
 #print(summationList)
 for i in summationList:
  incrementer += len(i)
#poggers
print(incrementer)
