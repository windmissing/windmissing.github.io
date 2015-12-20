compareCnt = 0

def compare(a, b) :
    global compareCnt
    compareCnt += 1
    return a < b

def findSmallest( array ) :
    min, minId = array[0], 0
    array = array[ 1 : ]
    for index, element in enumerate ( array ) :
        if compare(element, min) :
            min, minId = element, index
    return minId

def findSecondSmaller( array, minId ) :
    array = array[ : minId ] + array[ minId+1 : ]
    array = array[ 1 : ]
    secondSmaller = array[0]
    for element in array :
        if compare(element , secondSmaller) :
            secondSmaller = element
    return secondSmaller

def solution ( array ) :
    smallestId = findSmallest( array )
    smaller = findSecondSmaller ( array, smallestId )
    return smaller

array = [12, 34, 56]
print solution( array )
print compareCnt

