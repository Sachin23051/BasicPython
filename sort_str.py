
def sort_str(s1):
    arr =list(s1)
    n= len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                
    
    sorted_str ="".join(arr)
    return sorted_str
    
print(sort_str("sachin"))