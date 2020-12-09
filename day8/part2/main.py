import copy

def noMoreSplits(accumulator, position, array):
 opcode = array[position].split()
 #Basically, we go through the array of instructions and quit if we run into a loop.
 while len(array) > position:
  opcode = array[position].split()
  if opcode[0] == "visited":
   #If we have a loop, get out of the function asap! 
   return()
  elif opcode[0] == 'acc':
   accumulator += int(opcode[1])
   array[position] = "visited " + array[position]
   position += 1
   if len(array) < position:
    print(accumulator)
    quit
  elif opcode[0] == 'jmp' :
   array[position] = "visited " + array[position]
   position += int(opcode[1])
   if len(array) < position:
    print(accumulator)
    quit
  elif opcode[0] == 'nop':
   array[position] = "visited " + array[position]
   position += 1
   if len(array) < position:
    print(accumulator)
    quit
 #If we get out, that means that we've gotten through instructions without any loops! 
 #Print accumulator ^^;
 print(accumulator)



with open("input.txt", "r") as f: 
 array = f.read().split('\n')

#This removes an empty element at the back of the array.
array.pop()
accumulator = 0
position = 0
opcode = array[position].split()
#while opcode[0]:
while len(array) > position:
 #Split our line into a list of strings
 opcode = array[position].split()
 #If we've visited, quit.
 if opcode[0] == "visited":
  quit()
 #Accumulate. Nothing too special
 elif opcode[0] == 'acc':
  accumulator += int(opcode[1])
  array[position] = "visited " + array[position]
  position += 1
 #jmp. This gets interesting!
 elif opcode[0] == 'jmp' :
  #add "visited" to this element in the array
  array[position] = "visited " + array[position]
  #make a positionNoSplit to pass into our function. positionNoSplit acts as if our current instruction was an 'nop'
  positionNoSplit = position + 1
  #Same thing, but with accumulator.
  accumulatorNoSplit = accumulator
  #IMPORTANT: we need to DEEP COPY our array. This gives noMoreSplits it's own memory, with its own array
  arrayNoSplit = copy.deepcopy(array)
  #Call noMoreSplits, which will run as if current command was a 'nop'.
  noMoreSplits(accumulatorNoSplit, positionNoSplit, arrayNoSplit)
  #increment our own position and keep running.
  position += int(opcode[1])
 #'nop'. Again, nothing special here.
 elif opcode[0] == 'nop':
  array[position] = "visited " + array[position]
  position += 1
#if we've gotten out of the while loop, that means the opcode had no cycles! 
#We get to print our accumulator c:
print(accumulator)
