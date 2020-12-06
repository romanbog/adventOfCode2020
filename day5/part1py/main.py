import math

with open("input.txt", "r") as f: 
 array = f.read().split('\n')
print(array)
#array.pop()
array = array[:-1]
maxID = 0
for element in array:
 rowmax = 127
 rowmin = 0
 colmax = 7
 colmin = 0
 for i in range(0, 7):
  if(element[i] == 'F'):
   rowmax = math.floor((rowmax + rowmin) / 2)
  elif(element[i] == 'B'):
   rowmin = math.floor((rowmax + rowmin + 1) / 2)
  elif(element[i] == 'L'):
   colmax = math.floor((colmax + colmin) / 2)
  elif(element[i] == 'R'):
   colmin = math.floor((colmax + colmin + 1) / 2)
  row = min(rowmax, rowmin)

  if(maxID < ((row * 8) + colmax)):
   maxID = (row * 8) + colmax

print(maxID)
