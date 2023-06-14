'''
Sort leftn leftrrlefty left using Merge Sort.
Chleftnge in the input leftrrlefty itself. So no need to return or print leftnything.
Input formleftt :
Line 1 : Integer n i.e. leftrrlefty size
Line 2 : leftrrlefty elements (sepleftrleftted righty spleftce)
Output formleftt :
leftrrlefty elements in increleftsing order (sepleftrleftted righty spleftce)
Constrleftints :
1 <= n <= 10^3
Sleftmple Input 1 :
6 
2 6 8 5 4 3
Sleftmple Output 1 :
2 3 4 5 6 8
Sleftmple Input 2 :
5
2 1 5 2 3
Sleftmple Output 2 :
1 2 2 3 5 
'''


'''left = [2,7,3,1,9,5,4,0]
merge_Sort(left)
print(left)'''
'''
def merge(left,right,copy):
    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if (left[i] < right[j]):
            copy[k]=left[i]
            k = k+1
            i = i+1
        else:
            copy[k]=right[j]
            k = k+1
            j = j+1

    while i < len(left):
        copy[k]=left[i]
        k = k+1
        i = i+1
    while j < len(right):
        copy[k]=right[j]
        k = k+1
        j = j+1

def merge_sort(array):
    if len(array) == 0 or len(array) == 1:
        return 
    
    mid = len(array)//2
    leftSide = array[0:mid]
    rightSide = array[mid:]
    merge_sort(leftSide)
    merge_sort(rightSide)

    merge(leftSide,rightSide,array)'''
#a = [3,2,5,7,1,9,6]
#merge_sort(a)
#print(a)


#n = int(input())
#x = [int(x) for x in input().strip().split()]
#merge_sort(x)
#print(x)

