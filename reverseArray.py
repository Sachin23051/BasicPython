arr=[1,2,3,5,6,22,3]
n=len(arr)
new_arr =[]
for i in range(n-1,-1,-1):
    new_arr.append(arr[i])
    
print(new_arr)