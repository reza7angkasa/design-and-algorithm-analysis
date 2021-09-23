def SelectionSort(list):
    for fill_slot in range(len(list) -1,0,-1):
        max_index= 0
        for location in range(1,fill_slot+1):
            if list[location]>list[max_index]:
                max_index=location
        list[fill_slot],list[max_index]=list[max_index],list[fill_slot]
        return list
list=[89,12,57,16,25]
SelectionSort(list)
print(list)