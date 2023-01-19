import pdb

def callPermu(a):
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
        #pdb.set_trace()
        #print(head)
        #print('tail')
        #print(tail)

        for j,ks in enumerate(tail) :
            temp1 = []
            temp1.append(head)
            for k,k1 in enumerate(ks):
                temp1.append(k1)
            result.append(temp1)
        #temp.append(head)
    return result

def test() :
    callPermu(temp)
    #print(tail)
    for j,k1 in enumerate(tail) :  # in range(count - 1):
        ks = [] #head]
        ks.append(head)
        for k,k2 in enumerate(k1):
            ks.append(k2)
            result.append(ks)
            
    return result

start = []  #1,2,3]
for i in range(9):
    start.append(i+1)
    
result = callPermu(start)
print(result)
print(len(result))
#for i,ks in enumerate(result):
#    print(ks)
#    pass
                      
        
