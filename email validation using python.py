print("Welcome to our Email validation project..!\n")
email = input("Enter Your Email for validation:")  # a@a.in  a@a.com

upperr = 1
splchar = 1
space = 1

if len(email) >= 6:
    if email[0].isalpha():
        if "@" in email and email.count("@") == 1:
            if email[-4] == "." or email[-3] == ".":
                for i in email:
                    if i.isspace():
                        space = 0  #same as flag menas it is false then it is 0
                    elif i.isalpha():
                        if i.isupper():
                            upperr = 0
                    elif i.isdigit():
                        continue
                    elif i == "_" or i == "." or i == "@":
                        continue
                    else:
                        splchar = 0
                if space == 1 and upperr == 1 and splchar == 1:
                    print("Hurray, Your Email is valid..\n")
                else:
                    print("Wrong Email syntax.\nPlease, enter a correct email.\n")
            else:
                print("Email should contain at least one dot.\nPlease, enter a correct email.\n")
        else:
            print("There should be only one '@'\nPlease, enter a correct email.\n")
    else:
        print("First letter is not an alphabet.\nPlease, enter a correct email.\n")
else:
    print("Email length should be at least 6 characters.\nPlease, enter a correct email.\n")
