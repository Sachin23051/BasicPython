from collections import defaultdict

def sort_str(s):
    s1 =list(s)
    n= len(s1)
    for i in range(n):
        for  j in range(0,n-i-1):
            if s1[j]>s1[j+1]:
                s1[j],s1[j+1]=s1[j+1],s1[j]

    str_sort="".join(s1)
    return str_sort



def anagram(arr):
    thisdict = defaultdict(list)
    for s in arr:
        sort_s =sort_str(s)
        thisdict[sort_s].append(s)

    return thisdict.values()

 

print(anagram(['abc','bca','cab','eat','ate','tea']))
