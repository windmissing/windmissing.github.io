compareCnt = 0
comparePath = [i for i in range(10), []] 

def compare(a, b) :
    global compareCnt
    compareCnt += 1
    return a < b

def findSmallest( array ) :
    global comparePath
    min, minId = array[0], 0
    for i in range( 1, len(array) ) :
        if compare(array[i] , min) :
            comparePath[i].append(min)
            min, minId = array[i], i
        else :
            comparePath[minId].append(array[i])
    return minId

def findSmaller( minId ) :
    global comparePath
    sec = comparePath[minId][0]
    for element in comparePath[minId] :
        if compare(element , sec) :
            sec = element
    return sec

def solution ( array ) :
    smallestId = findSmallest( array )
    smaller = findSmaller ( smallestId )
    return smaller

array = [12, 34, 56]
print solution( array )
print compareCnt

