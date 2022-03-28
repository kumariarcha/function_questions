from cgitb import small


def strong_password(password):
    digit="0123456789"
    capital_alpabeat="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    small_alhphabet="abcdefghijklmnopqrstuvwxyz"
    special_char="@#$_"
    sum=0
    a=0
    x=0
    y=0
    z=0
    if len(password)>6 or len(password)<=16:
        i=0
        while i<len(password):
            if password[i] in digit:
                x=1
            elif password[i] in capital_alpabeat:
                y=1
            elif password[i] in small_alhphabet:
                z=1
            elif password[i] in special_char:
                a=1
            i=i+1
        sum=x+y+z+a
        if sum<4:
            print("password should have atlest one capital one small one char on digit")
        else:
            print("strong password")
password=input("enter the password")
strong_password(password)


