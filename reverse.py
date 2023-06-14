'''def magicIndex(array,element):
    if len(array)==0:
        return
    for i in range(len(array)):
        if array[i] == element:
            return i

ar = [0,1,3,3]
print(magicIndex(ar,3))'''
'''arr = [0,1,2,4,5,7,6]
for i in range(len(arr)):
    #print(arr[i], i)
    if arr[i] == i:
        print(arr[i])'''
'''n = int(input())
l1 = []
for i in range(n):
    total = int(input())
    l1.append(total)
print(l1)
'''
'''
def binarySearch(array, search, start,end):
    if len(array) == 0:
        return
    
    mid = (start+end)//2

    for i in array:
        if search not in array:
            return "Value not found"

    if array[mid]==search:
        return mid
    elif array[mid]>search:
        return binarySearch(array,search,start-1,end)
    else:
        return binarySearch(array,search,start,end+1)

'''
'''a = 9
if a>5 and a<9:
    print("Hi")
else:
    print("uff")'''
'''n = input()
vowels = "aeiou"
if vowels in n:
    print()'''
'''x,y = [int(i) for i in input().split()]
if(x<y):
    st = "x is less than y"
    print(st)'''

# Python program to check if the number is an Armstrong number or not

'''
num = int(input("Enter a number: "))

sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")'''


'''n = int(input())
for i in range(n):
    if n == str(n[::-1]):
        print("p")'''

'''n = int(input())
for i in range(n):
    x = [int(i) for i in input().split()]
    for j in range(len(x)):
        #print(x[j],j)
        print(x[j]**3 + )'''
'''l1 = [1,2,3]
sum = 0
for i in range(len(l1)):
    print(l1[i]**3,end=" ")
   '''
'''x = [int(i) for i in input()]
for i in range(len(x)):
    if x[-1]%3 == 0:
        print("Divisible")
    else:
        print("Not diivisible")
    break
print(x[-1])'''

