def Duplicate_num(arr):
    n= len(arr)
    seen=set()
    duplicate=set()
    for x in arr:
        if x in seen:
            duplicate.add(x)
        else :
            seen.add(x)
        
    print(duplicate)


Duplicate_num((1,2,3,4,45,7,3,2,1))