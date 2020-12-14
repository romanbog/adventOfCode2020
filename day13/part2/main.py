from functools import reduce
from operator import mul

def chinese_remainder(input):
    m = [i[0] for i in input]
    a = [i[0]-i[1] for i in input]
    mm = reduce(mul,m,1)
    z = [mm // mi for mi in m]
    y = [pow(i,-1,j) for i,j in zip(z,m)]
    w = [(i*j)% mm for i,j in zip(y,z)]
    return  sum((a*w) for a,w in zip(a,w)) % mm

with open("input.txt", "r") as f: 
 array = f.read().split('\n')

arrivalTime = int(array[0])
busIDList = array[1].split(',')
tupleList = []

for index, bus in enumerate(busIDList):
 if bus == 'x':
  pass
 else:
  thisTuple = (int(bus), index)
  tupleList.append(thisTuple)

print(tupleList)

print(chinese_remainder(tupleList))

print(tupleList)
