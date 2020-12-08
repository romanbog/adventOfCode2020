with open("input.txt", "r") as f: 
 array = f.read().split('\n')

accumulator = 0
#for every group
position = 0
opcode = array[position].split()
while opcode[0]:
 opcode = array[position].split()
 if opcode[0] == "visited":
  print(accumulator)
  quit()
 elif opcode[0] == 'acc':
  #print(array[position])
  accumulator += int(opcode[1])
  array[position] = "visited " + array[position]
  position += 1
 elif opcode[0] == 'jmp' :
  #print(array[position])
  array[position] = "visited " + array[position]
  position += int(opcode[1])
 elif opcode[0] == 'nop':
  #print(array[position])
  array[position] = "visited " + array[position]
  position += 1
print(accumulator)
