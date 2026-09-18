a=int(input())
b=int(input())
c=str(input())
if  c == "add":
    print(a+b)
elif c == "sub":
    print(a-b)
elif c=="div":
    if b == 0:
        print("Cant Divide with 0")
    else:
        print(a/b)
elif c=="mul":
    print(a*b)
    


