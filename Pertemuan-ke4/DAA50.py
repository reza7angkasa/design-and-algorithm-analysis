def BubbleSort(list):
    lastElementIndex=len(list)-1
    for passNo in range(lastElementIndex,0,-1):
        for idx in range(passNo):
            if list[idx]>list[idx+1]:
                list[idx],list[idx+1]=list[idx+1],list[idx]
    return list
list=[100,20,60,90,40,30,10]
BubbleSort(list)
print(list)
