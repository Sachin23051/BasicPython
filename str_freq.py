def count_char(s1):
    s=s1.lower()
    thisdict ={}
    for x in s:
        if x in thisdict:
            thisdict[x]+=1
        else:
            thisdict[x]=1
    return thisdict
    

    
def str_dic(s):
    dic=count_char(s)
    str_new=""
    for k,v in dic.items():
        str_new = str_new + k +str(v)
    return str_new
            
print(str_dic("Engineer"))