try:
    num1=int(input("enter num1 :"))
    num2=int (input("enter num2 :"))
    min =num1
    if num2>min:
        min=num2

    while min>=1:
        if num1%min==0 and num2%min==0 :
            break
        min-=1

except ValueError:
    print("oops ! YOU DID NOT GIVE ME 2 DIGITS")

else:
    print("result is :",min)