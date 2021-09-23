def InsertionSort(list):
    for i in range(1, len(list)):
        j=i-1
        next=list[i]
        while (list[j]>next)and(j>=0):
            list[j+1]=list[j]
            j=j-1
        list[j+1]=next
    return list
list=[89,312,57,16,25,11,75]
print(list)
InsertionSort(list)
print(list)
