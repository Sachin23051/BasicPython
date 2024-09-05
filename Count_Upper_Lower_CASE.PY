def count_UL(s1):
    no_lower=0
    no_upper=0
    no_space=0
    for c in s1:
        if c.islower():
            no_lower+=1
        elif c.isupper():
            no_upper+=1
        elif c.isspace():
            no_space +=1
            
    print(no_lower)
    print(no_upper)
    print(no_space)
    
count_UL("Sachin Gupta")