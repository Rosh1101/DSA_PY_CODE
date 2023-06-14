'''a = "roshan"
el = "aeiou"
for i in el:
    if i in a:
        print(i)'''

'''a = "pythin is cool"
print(a.replace("cool","eww but awesome and great"))'''
'''
def counton(string):
    if len(string) == 0:
        return 0

    count = 0
    
    for i in string:
        if i == " ":
            count+=1
    return count+1

    
string = "A world"
count = counton(string)
'''


from sys import stdin


def countWords(string) :
	# Your code goes here
    
    if len(string) == 0:
        return 0
    
    count = 0
    for i in string:
        if i == ' ':
            count += 1
            
            
    return count + 1
























	



#main
string = stdin.readline().strip();
count = countWords(string)

print(count)


