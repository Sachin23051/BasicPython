#Method1
def sumPair(arr,Target):
    for i in arr:
        for j in arr:
            if i+j==Target:
                print([i,j])

sumPair([2,4,20,40,60,80,90],100)

# methods 
def method2(arr,target):
    seen=set()
    pairs=[]
    for num in arr:
        compliment=target-num
        if compliment in seen:
            pairs.append((compliment,num))
        
        seen.add(num)
    return pairs

print(method2([30,70,40,60,80,20],100))
