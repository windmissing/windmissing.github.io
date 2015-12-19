compareCnt = 0

def compare(a, b) :
    global compareCnt
    compareCnt += 1
    return a < b

def findSmallest( array ) :
    min, minId = array[0], 0
    for i in range( 1, len(array) ) :
        if compare(array[i] , min) :
            min, minId = array[i], i
    return minId

def findSmaller( array, minId ) :
    if minId == 0 :
        sec, secId = array[1], 1
    else :
        sec, secId = array[0], 0
    for i in range( 0, len(array) ) :
        if i != minId and compare(array[i] , sec) :
            sec, secId = array[i], i
    return sec

def solution ( array ) :
    smallestId = findSmallest( array )
    smaller = findSmaller ( array, smallestId )
    return smaller

array = [12, 34, 56]
print solution( array )
print compareCnt

