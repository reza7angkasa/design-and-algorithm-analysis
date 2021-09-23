def BubbleSort(list):
    lastElementIndex=len(list)-1
    for passNo in range(lastElementIndex,0,-1):
        for idx in range(passNo):
            if list[idx]>list[idx+1]:
                list[idx],list[idx+1]=list[idx+1],list[idx]
    return list

def BinarySearch(list,item):
    first=0
    last=len(list)-1
    found=False
    while first<=last and not found:
        midpoint=(first+last)//2
        if list[midpoint]==item:
            found=True
        else:
            if item < list[midpoint]:
                last=midpoint-1
            else:
                first=midpoint+1
    return found
    
list=['y','u','i','w','o','a','q','u','j','p']
sorted_list=BubbleSort(list)
print(BinarySearch(list,'a'))