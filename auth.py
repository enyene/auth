import random

database = {}
balance = 0


def init():
    isValidOption = False
    print("welcome")
    while  isValidOption == False:
        haveAccount = int(input("do you have account with us 1.(yes) 2.(no)\n"))
        if haveAccount == 1:
            isValidOption = True
            login()
        elif (haveAccount == 2):
            isValidOption = True
            register()
        else:
            print("you have selected invalid options")


def register():
    print("register")
    email = input("what is your email?\n")
    firstName = input("what is your first name?\n")
    lastName = input("what is your last name?\n")
    password = input("choose a password\n")

    accountNumber = accountNumberGeneration()

    database[accountNumber] = (firstName, lastName, email, password)
    print("your account have been created successfully")
    print("your account number is %d" % accountNumber)
    login()


def login():
    print("login to your acccount")
    accountNumberInput = int(input("what is your account number\n"))
    password = input("what is your password\n")
    for accountNumber, userDetails in database.items():
        if accountNumber ==accountNumberInput:
            if userDetails[3] == password:
                operations(userDetails)
        else:
            print("invalio credentials please try again")
            login()


def accountNumberGeneration():
    return random.randint(1111111111, 9999999999)


def operations(user):
    print("welcome %s %s"%(user[0],user[1]))
    options = int(input("what operation would you like to perform 1.deposit 2.withdraw 3.log out 4.exit\n"))
    if options == 1:
        deposit()
    elif options == 2:
        withdrawal()
    elif options == 3:
        login()
    elif options == 4:
        exit()
    else:
        print("invalid option selected")
        operations(user)



def withdrawal():
    print("withdraw")
    withdrawnAmount = int(input("How much do you want to withdraw\n"))
    print('You have withdrawn %i ' % withdrawnAmount)
    print('Take your cash')



def deposit():
    balance = 0
    print("deposit")
    depositAmount = int(input('How much would you like to deposit\n'))
    balance = balance + depositAmount
    print("you have deposited %d"%depositAmount)
    print('Your current balance is %i' % balance)


def complaints():
    complain = input('What issue would you like to report\n')
    print('Thank you for contacting us , we will respond shortly')


init()
