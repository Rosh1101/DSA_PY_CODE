'''def replace(string,a,b):
    if len(string) == 0:
        return string
    
    small_output = replace(string[1:],a,b)
    if string[0] == a:
        return b+small_output
    else:
        return string[0]+small_output
print(replace("davasafa","a","x"))
'''



def replace(string,replace_me,to_be_replaced_with):

    #if the length is 0
    if len(string)==0:
        return string

    #if length is not zero
    small_output = replace(string[1:],replace_me,to_be_replaced_with)
    if string[0] == replace_me:
        return to_be_replaced_with+small_output
    else:
        return string[0]+small_output
print(replace("acdaavasa","a","x"))

def replaceX(string,replace,replace_with):
    if len(string)==0:
        return 
    not_first = replaceX(string[1:],replace,replaceX)
    if string[0] == replace:
        return replace_with+not_first
    else:
        return string[0]+not_first
print(replaceX('x','x','b'))