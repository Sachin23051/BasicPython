#reverse string 
def Rev_Str(str1):
    rev_str=""
    for c in str1:
        rev_str=c+rev_str
    return rev_str
    
    
def rev(str1):
    return str1[::-1]

print(rev("sabhi"))
print(Rev_Str("sachin"))