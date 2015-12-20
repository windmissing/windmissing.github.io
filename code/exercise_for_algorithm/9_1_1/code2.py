compareCnt = 0 

def compare(a, b) :
    global compareCnt
    compareCnt += 1
    return a < b

def findSmallestAndCollectInformation( array ) :
    comparePath = [ [] for i in range(len(array))]
    smallest, smallestId = array[0], 0
    array = array[ 1 : ]
    for index, element in enumerate ( array ) :
        if compare(element , smallest) :
            comparePath[index].append(smallest)
            smallest, smalleId = element, i
        else :
            comparePath[smallestId].append(element)
    return comparePath[smallestId]

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
print solution( array )
print compareCnt

