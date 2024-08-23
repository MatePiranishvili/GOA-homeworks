print ("please creat new bank account")
print("please neter your name,remember name needs to be over 8 symblos")
name =  input("please enter your account name: ")




print("deposit money")

money = int(input("please enter amount of money you want to deposit  :"))
if money > 1000000:
    print("you cant deposit that amount of money in this program")
else:
    print("you succsesfully deposited money")


print("do you want to withdraw money?")
print("first you have to prove that you are owner of this bank account")
password1 = int(input("please enter you password:"))
if password1 == 2222 :
    print("password is corecct ")
else:
    print("password is inccorect!")
print("now you have to do the kapthca")

# kaptcha = print(True and False)
# kaptcha = print(True or False )

kaptcha = input("please enter your kaptcha")
if kaptcha == "true and false #True ,True or false #true":
    print("you answered kaptcha corecctly")
else:
    print("try again")


print("do you want to leave this website?")
print("type exit here to log off")
exit = input("type exit here to log off")
if exit == exit:
    print("you logged off succsesfuly")
else:
    print("you are still on the website.")