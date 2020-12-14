with open("example.txt", "r") as f: 
 array = f.read().split('\n')

array.pop()

busIDList = array[1].split(',')
memory = []
mask = []

for command in array:
 commandSplit = command.split(' = ')
 if commandSplit[0] == 'mask':
  print("mask here")
  for index, character in enumerate(commandSplit[1]):
   if index != 'X':
    mask[index] = int(character)
   else:
    mask[index] == 99
  print(mask)
 else:
  print("memory here")
