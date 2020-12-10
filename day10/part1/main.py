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

for element in joltList:
 if joltList.index(element) + 1 ==  len(joltList):
  break
 if joltList[joltList.index(element) + 1] == element + 1:
  oneDifference += 1
 elif joltList[joltList.index(element) + 1] == element + 2:
  twoDifference += 1
 elif joltList[joltList.index(element) + 1] == element + 3:
  threeDifference += 1

print(oneDifference)
print(twoDifference)
print(threeDifference)
print(oneDifference * threeDifference)
