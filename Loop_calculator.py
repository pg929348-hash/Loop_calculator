while True:
    a= float(input("enter 1st number:"))
    b= (input("enter operators: +,-,*,/,exit:"))
    if b=="exit":
        print (" calculator exit")
        break
    c= float (input ("enter 2nd number:"))
    if b=="+":
        print ("result:",a+c)
    elif b=="-":
        print ("result:",a-c)
    elif b=="*":
        print ("result:",a*c)
    elif b=="/":
        if c!=0:
            print ("result:",a/c)
        else:
            print ("error: can't divided by 0")
    else:
        print ("invalid operator ")
