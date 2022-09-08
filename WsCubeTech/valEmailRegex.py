import re 
# starts with a-z
# has an underscore  
# has zero or one occurance of any character a-z 0-9
# has an @
#has a dot
#contains any character 

# contains any character of length 2, 3
def valEmReg():
    email_condition="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
    user_email=input("What's you're email : " )
    if re.search(email_condition, user_email):
        print("Right Email")
    else:
        print("Wrong Email")