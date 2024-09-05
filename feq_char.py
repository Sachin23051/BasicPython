
def freq_char(input_str):
    feq={}
    for c in input_str:
        if c in feq:
            feq[c]+=1
        else:
            feq[c]=1
    print(feq)

def sort_feq(s1):
    n= len(s1)
    for i in range(n):
        for j in range(0,n-i-1):
            if s1[j]>s1[j+1]:
                s1[j],s1[j+1]=s1[j+1],s1[j]

   


            
            



freq_char("nayan")