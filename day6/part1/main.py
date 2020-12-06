with open("input.txt", "r") as f: 
 array = f.read().split('\n\n')

summation = 0
#for every group
for element in array:
 #replace newlines
 string = element.replace("\n", "" )
 #join all in set string with onlyunique
 onlyunique = ''.join(set(string))
 #add length of unique answers to summation
 summation += len(onlyunique)

print(summation)
