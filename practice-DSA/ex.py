'''a = [1,3,2,6,4,9,7,55,6]
print(a)
a.sort()
print(a)'''


def replaceChar(string,replace,replace_with):
    if len(string) == 0:
        return string
    
    smallOut = replaceChar(string[1:],replace,replace_with)
    if string[0] == replace:
        return replace_with+smallOut
    else:
        return string[0]+smallOut

print(replaceChar("xxxa","x","a"))
