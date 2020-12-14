import time
import multiprocessing as mp
import itertools 

def isEqual(inputNumber):
 if inputNumber == 69690696:
  return True
 else:
  return False

def isEqualPara(inputNumber):
 if inputNumber == 70:
  return inputNumber
 else:
  return 0
'''
def getResult(result):
 if result == True:
  pool.close()
  pool.join()
  GlobeResult = result
'''
def simple():
 print("process called")

start = time.time()

toCheck = 0
'''
while True:
 if isEqual(toCheck):
  break
 toCheck += 1
'''
end = time.time()

print("Linear result: ", toCheck)
print(end - start)

start = time.time()
simple()


pool = mp.Pool(mp.cpu_count())

def getResult(result):
 #print(result)
 if result > 0:
  GlobeResult = result
  pool.terminate()

toCheck = 0
global GlobeResult
GlobeResult = 0
#while GlobeResult == 0:
#while True:
for i in itertools.repeat(1):
#for i in range(100):
 print(toCheck)
 pool.apply_async(isEqualPara, args = (toCheck, ), callback = getResult)
 toCheck += 1

pool.close()
pool.join()


end = time.time()

print("Linear result 2: ", toCheck)
print(end - start)
