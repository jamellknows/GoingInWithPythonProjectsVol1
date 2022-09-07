from curses.ascii import isalpha


def emailValidate():
    email = input("Enter your email : ")
    k,j,d =0,0,0
    if len(email) >= 6:
        if(email[0].isalpha()):
            if("@"in email) and (email.count("@")==1):
                if(email[-4] ==".") ^(email[-3]=="."):
                    for i in email:
                        if i ==i.isspace():
                            k = 1
                        elif i.isalpha():
                            if i == i.upper():
                                j = 1
                        elif i.isdigit():
                            continue
                        elif i =="_" or i=="." or i =="@":
                            continue
                        
                        else:
                            d=1

                    if k == 1 or j == 1 or d ==1:
                        print("Email address cannot contain any spaces")
                else:
                    print("Email must have a dot before domain")

            else:
                print("Email Address must contain an @")

        else:
            print("Email must not contain a capital letter at the start ")

    else:
        print("Email must hav a length greater than 6 ")