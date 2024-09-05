def SecondHighest(arr):
    highest=0
    Secondhighest=0
    for x in arr:
        if x >highest :
            Secondhighest=highest
            highest =x
             
             
        if x>Secondhighest and x !=highest:
            Secondhighest =x
    
    print(Secondhighest)
    
arr=[12, 35, 1, 10, 34, 1, 35]
SecondHighest(arr)