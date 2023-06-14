def removeDumplicateString(string):
    if len(string) == 0 or len(string) == 1:
        return string
    
    if string[0]==string[1]:
        smallOut = removeDumplicateString(string[1:])
        return smallOut

    else:
        smallOut = removeDumplicateString(string[1:])
        return string[0]+smallOut
print(removeDumplicateString("aabbacc"))