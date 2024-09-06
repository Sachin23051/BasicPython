# method1
def com_elmt(l1,l2):
    new_list =set()
    for i in l1:
        for j in l2:
            if i==j:
                new_list.add(i)
    print(new_list)

com_elmt([1,2,3,4],[3,4,3])


# method2
def method2(l1,l2):
    set1=set(l1)
    set2=set(l2)
    common =set1.intersection(set2)
    return common


print(method2([2,3,4,5,5],[2,4,5,6,7,7]))
