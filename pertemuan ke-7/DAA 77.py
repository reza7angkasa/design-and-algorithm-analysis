def Sequential_Search(dlist, item):
    pos=0
    found= False
    while pos < len(dlist) and not found:
        if dlist[pos]==item:
            found=True
        else:
            pos=pos+1
    return found,pos
print(Sequential_Search(['a','b','c','d','e','f','g','h'],'g')) 