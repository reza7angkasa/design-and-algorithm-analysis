def LinearSearch(list,item):
    index=0
    found=False
    while index<len(list) and found is False:
        if list[index]==item:
            found=True
        else:
            index=index+1
    return found
list=['y','u','i','w','o','a','q','u','j','p']
print(LinearSearch(list,'a'))