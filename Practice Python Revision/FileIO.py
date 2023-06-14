#writing a file

n = input("Enter the number to be sent to file: ")
with open("IOONE.txt","w") as sent:
    sent.write(n)

#Reading a file
with open("IOONE.txt","r") as f:
    a = f.read()
    print(a)