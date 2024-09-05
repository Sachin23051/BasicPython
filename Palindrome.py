#reverse string 
def Palindrome(s1):
    str1=s1.lower().strip()
    rev_str=""
    for c in str1:
        rev_str=c+rev_str
    if rev_str ==str1:
        print(f" {s1} is Plaindrome")
    else:
        print(f"{s1} is Not palindrome")
    



Palindrome("Nayan ")