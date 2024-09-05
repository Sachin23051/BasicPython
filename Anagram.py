
def sort_str(s1):
    arr =list(s1)
    n= len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                
    
    sorted_str ="".join(arr)
    return sorted_str
    
def anagram(str1,str2):
    if len(str1)==len(str2):
        n_str1=sort_str(str1)
        n_str2=sort_str(str2)
        if n_str1 == n_str2:
            print("Given String Anagram")
        
    else:
        print("Given String is Not Anagram")
        
anagram("sach","cash")
