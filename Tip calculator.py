 #calculating tip

#tip function
def tip():
    bill=int(input("Enter bill amount / 0 to exit the calculator  \n"))

    if bill>0:
        x=float((bill / 100) * 20)
        print("your Tip is ",x)
        tip()
    elif bill==0:
        print("you have exited the calculator")
        exit 
    else:
        print("invalid amount ")
        print("please ",end='')
        tip()

tip()

#close the application
input("Press 'Enter' to exit the app")