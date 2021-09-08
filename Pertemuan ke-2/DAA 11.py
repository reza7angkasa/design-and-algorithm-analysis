def getSum(myList):
  sum = 0 
  for row in myList:
      for item in row:
          sum += item
  return sum
getSum([[1,2,5],[3,4,7]])