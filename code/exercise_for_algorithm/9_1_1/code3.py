compareCnt = 0 

def compare(a, b) :
    global compareCnt
    compareCnt += 1
    return a < b

def findSmallestAndCollectInformation( array ) :
    indexList = [ i for i in range(len(array)) ]
    comparePath = [ [] for i in range(len(array)) ]
    while len(indexList) != 1 :
        indexList = compareAndStore(array, indexList, comparePath)
    return comparePath[indexList[0]]

def compareAndStore(array, indexList, comparePath) :
    tempIndexList = []
    indexCount = len( indexList )
    for i in range( int((indexCount)/2) ) :
        f = lambda : indexCount-i-1
        if compare ( array[indexList[i]] , array[indexList[f()]] ) :
            comparePath[indexList[i]].append(array[indexList[f()]])
            tempIndexList.append(indexList[i])
        else :
            comparePath[indexList[f()]].append(array[indexList[i]])
            tempIndexList.append(indexList[f()])
    if indexCount % 2 != 0 :
        tempIndexList.append(indexList[int(indexCount/2)])
    return tempIndexList

def findSecondSmaller( comparePath ) :
    secondSmaller = comparePath[0]
    comparePath = comparePath [ 1 : ]
    for element in comparePath :
        if compare(element , secondSmaller) :
            secondSmaller = element
    return secondSmaller

def solution ( array ) :
    global compareCnt
    compareCnt = 0
    comparePathBySmallest = findSmallestAndCollectInformation( array )
    secondSmaller = findSecondSmaller ( comparePathBySmallest )
    return secondSmaller

array = [12, 34, 56]
assert ( 34 == solution( array ))
print compareCnt
array = [54, 32, 10]
assert (32 == solution( array ))
print compareCnt

