with open("input.txt", "r") as f: 
 array = f.read().split('\n')

accumulator = 0
#where we're located in our array.
position = 0
opcode = array[position].split()
while len(array) > position:
 #split our instruction into a list of strings
 opcode = array[position].split()
 #If the first element of our instruction is "visited", print accumulator and quit.
 if opcode[0] == "visited":
  print(accumulator)
  quit()
 #If we have an 'acc', update acumulator and go forward one
 elif opcode[0] == 'acc':
  accumulator += int(opcode[1])
  #append "visited" to mark that our string has been visited
  array[position] = "visited " + array[position]
  position += 1
 #If we have 'jmp', update position based on jmp's value.
 elif opcode[0] == 'jmp' :
  #append "visited" to mark that our string has been visited
  array[position] = "visited " + array[position]
  position += int(opcode[1])
 #If we have an 'nop', just move forward once.
 elif opcode[0] == 'nop':
  #append "visited" to mark that our string has been visited
  array[position] = "visited " + array[position]
  position += 1
print(accumulator)
