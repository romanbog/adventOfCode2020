import copy

def noMoreSplits(accumulator, position, array):
 opcode = array[position].split()
 while len(array) > position:
  opcode = array[position].split()
  if opcode[0] == "visited":
   #print("quit in nosplits")
   return()
  elif opcode[0] == 'acc':
   #print(array[position])
   accumulator += int(opcode[1])
   array[position] = "visited " + array[position]
   position += 1
   if len(array) < position:
    print(accumulator)
    quit
  elif opcode[0] == 'jmp' :
   #print(array[position])
   array[position] = "visited " + array[position]
   position += int(opcode[1])
   if len(array) < position:
    print(accumulator)
    quit
  elif opcode[0] == 'nop':
   #print(array[position])
   array[position] = "visited " + array[position]
   position += 1
   if len(array) < position:
    print(accumulator)
    quit
 print(accumulator)



with open("input.txt", "r") as f: 
 array = f.read().split('\n')

array.pop()
#print(array)
accumulator = 0
position = 0
opcode = array[position].split()
while opcode[0]:
 opcode = array[position].split()
 if opcode[0] == "visited":
  quit()
 elif opcode[0] == 'acc':
  #print(array[position])
  accumulator += int(opcode[1])
  array[position] = "visited " + array[position]
  position += 1
 elif opcode[0] == 'jmp' :
  #print(array[position])
  #print(opcode)
  array[position] = "visited " + array[position]
  #positionNoSplit = position + 1
  #arrayNoSplit = array
  #accumulatorNoSplit = accumulator
  arrayNoSplit = copy.deepcopy(array)
  accumulatorNoSplit = copy.deepcopy(accumulator)
  positionNoSplit = copy.deepcopy(position) + 1
  noMoreSplits(accumulatorNoSplit, positionNoSplit, arrayNoSplit)
  #accumulatorYesSplit = accumulator
  #positionYesSplit = position + int(opcode[1])
  #arrayYesSplit = array
  #canStillSplit(accumulatorYesSplit, positionYesSplit, arrayYesSplit)
  position += int(opcode[1])
 elif opcode[0] == 'nop':
  #print(array[position])
  array[position] = "visited " + array[position]
  position += 1
print(accumulator)
