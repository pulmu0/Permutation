import pdb

def get_permutation(lists):
    if len(lists) <= 1 :
        return [lists]

    result = []
    for i,k in enumerate(lists):
        head = k
        tail = [x for j,x in enumerate(lists) if j != i ]
        tails = get_permutation(tail)  #list of list
        for j,tail in enumerate(tails):
            k1 = [head,*tail] #tail.insert(0,head)
            result.append(k1)

    return result

def callPermu(a):
    # a is list
    count = len(a)
    if count <= 1 :
        return [a]  # [[a[0]]]
    
    result = []  
    for i in range(count) :
        temp = []
        for j in range(count) : 
            if i == j :
                pass
            else:
                temp.append(a[j])
        head = a[i]
        tail = callPermu(temp)

        for j,ks in enumerate(tail) :
            temp1 = []
            temp1.append(head)
            for k,k1 in enumerate(ks):
                temp1.append(k1)
            result.append(temp1)
    return result


def test() :
    callPermu(temp)

    for j,k1 in enumerate(tail) :  # in range(count - 1):
        ks = [] #head]
        ks.append(head)
        for k,k2 in enumerate(k1):
            ks.append(k2)
            result.append(ks)
            
    return result

def testList():
    te = [1,3]
    s = [x for i,x in enumerate(te) if x  ]
    print(s)

start = []  #1,2,3]
for i in range(4):
    start.append(i+1)

print(start)
result = get_permutation(start) # callPermu(start)
print(len(result))
print(result)
#print(len(result))

#testList()

#for i,ks in enumerate(result):
#    print(ks)
#    pass
                      
        


