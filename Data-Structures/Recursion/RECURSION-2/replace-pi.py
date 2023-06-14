def replace(s):
    if len(s) == 0 or len(s) == 1:
        return s
    if s[0]=='p' and s[1]=='i':
        smallout = replace(s[2:])
        return "3.14"+smallout
    else:
        smallout = replace(s[1:])
        return s[0]+smallout
print(replace("roshpipiroshpi"))