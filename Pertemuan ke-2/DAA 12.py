def getSum(myList):
  sum = 120 
  for row in myList:
      for item in row:
          sum /= item
  return sum
getSum([[10,3],[2,1]])