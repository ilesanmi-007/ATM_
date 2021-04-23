import random
import sys
datas= {12345678: ['sam@gmail.com', 'sammy', 'ade', 1234, 1000], 87654321: ['chichi@qwerty', 'chichi', 'fatai', 1212, 1000] }
datas_for_another_bank = {12345678: ['sam@gmail.com', 'sammy', 'ade', 1234, 1000], 87654321: ['chichi@qwerty', 'chichi', 'fatai', 1212, 1000] }

def login():
    account_number = int(input('enter your account number: '))
    if account_number in datas:
        password = int(input('enter your password: '))
        if datas[account_number][3] != password:
            print('incorrect password')
            login()
        else:
            operations()
    else:
        print('invalid account number')
        acc = input('want to open an account y/n ')
        if acc.lower() == 'y' or acc.lower() == 'yes':
            opening_an_account()
        else:
            print('thanks for banking with us')
            sys.exit()

def opening_an_account():
    email = input('enter your email address: ')
    first_name = input('enter your first name: ')
    last_name = input('enter your second name: ')
    password = int(input('enter your password: '))
    confirm_password = int(input('re-enter password: '))
    if password == confirm_password:
         print('data saved. Please remember your pass word')
    else:
        print('password incorrect... Please re-enter details')
        opening_an_account()

        #generating account number
        
    account_number = random.randrange(000000000, 999999999)
    #print('your account number is {}'.format(account_number))
    datas[account_number] = [email, first_name, last_name, confirm_password, 1234]
    #return datas
    print('Your account has been created successfully...\n')
    print('your account details are {}'.format(datas[account_number]))
    print('...and your account number is {}'.format(account_number))
    print('now you can login: ')
    login()


def operations():
    print('what transaction do you want to make?')
    print('1. Deposit')
    print('2. Transfer')
    print('3. Withdrawal')
    print('4. Check balance')
    print('5. exit')
    transaction = int(input())
    if transaction == 1:
        deposit()
        response = input('\n want to perform another transaction? y/n')
        if response.lower() == 'y' or response.lower() == 'yes':
            operations()
        elif response.lower() == 'n' or response.lower() == 'no':
            print('thank you for using our service..')
            sys.exit()
        else:
            print('invalid response..')
        
    elif transaction == 2:
        transfer()
        
        

    elif transaction == 3:
        withdrawal()
        

    elif transaction == 4:
        check_balance()
        

    elif transaction == 5:
        print('Thank you for banking with us')
        sys.exit()
    else:
        print('you have entered an invalid option')
        operations()

def withdrawal():
    amount = float(input('how much do you want to withdraw? '))
    account_number = int(input('please reconfirm your account number: '))
    #print(datas[account_number][4])
    if amount > datas[account_number][4]:
        print('insufficient  balance')
    else:
        datas[account_number][4] = datas[account_number][4] - amount
    #remember to check if amount is greater or lesser than amount in account
    print('this is your balance: ', datas[account_number][4])

    response = input('do you want to perform another operation? y/n') #.......
    if response.lower() == 'y' or response.lower() == 'yes':
        operations()
    elif response.lower() == 'n' or response.lower() == 'no':
        print('thank you for using our services..')
        sys.exit()
    else:
        print('invalid response please')
    


def same_bank_transfer():
    account_number = int(input('please re-enter your account number: '))
    if account_number in datas:
        account_to_send_to = int(input('enter account number to send to '))
        amount = int(input('enter amount you wanna transfer '))
        if amount > datas[account_number][4]:
            print('insufficient balance')
        else:

            datas[account_to_send_to][4] = datas[account_to_send_to][4] + amount
            datas[account_number][4] = datas[account_number][4] - amount
    else:
        print('invalid account number please')
    
def different_bank_transfer():
    account_number = int(input('please re-enter your account number: '))
    if account_number in datas:
        account_to_send_to = int(input('enter account number of the bank to send to '))
        if account_to_send_to in datas_for_another_bank:
            amount = int(input('enter amount you wanna transfer '))
            if amount < datas[account_number][4]:
                datas_for_another_bank[account_to_send_to][4] = datas_for_another_bank[account_to_send_to][4] + amount
                datas[account_number][4] = datas[account_number][4] - amount
            else:
                print('insufficient balance..')
                response = input('want to perform another transaction? y/n ')
                if response.lower() == 'y' or response.lower() == 'yes':
                    operations()
                elif response.lower() == 'n' or response.lower() == 'no':
                    print('thank you for using our services..')
                    sys.exit()
        else:
            print('sorry..that account number doesnt exist')
    else:
        print("we don't have that account")

    response = input('do you want to perform another operation? y/n') #.......
    if response.lower() == 'y' or response.lower() == 'yes':
        operations()
    elif response.lower() == 'n' or response.lower() == 'no':
        print('thank you for using our services..')
        sys.exit()
    else:
        print('invalid response please')

        

# def balance():
#     print('your account balance is: ')
#     print(datas[account_number][4])


def transfer():
    print('Transferring to same bank or different bank')
    print('1. same bank')
    print('2. Another bank')
    response = int(input())
    if response == 1:
        same_bank_transfer()
        #need to create a function to sort this out
    elif response == 2:
        different_bank_transfer()

    else:
        print('invalid response')
        transfer()

def check_balance():
    account_number = int(input('please re-enter your account number: '))
    print('your account balance is ', datas[account_number][4])
    
    response = input('do you want to perform another operation? y/n') #.......
    if response.lower() == 'y' or response.lower() == 'yes':
        operations()
    elif response.lower() == 'n' or response.lower() == 'no':
        print('thank you for using our services..')
        sys.exit()
    else:
        print('invalid response please')
    


def deposit():
    amount = float(input('enter the amount you want to deposit? '))
    account_number = int(input('please re-enter your account number: '))
    datas[account_number][4] = datas[account_number][4] + amount

    print('\n your new balance is ', datas[account_number][4])
    response = input('do you want to perform another operation? y/n') #.......
    if response.lower() == 'y' or response.lower() == 'yes':
        operations()
    elif response.lower() == 'n' or response.lower() == 'no':
        print('thank you for using our services..')
        sys.exit()
    else:
        print('invalid response please')


print("__________ welcome to The King's Bank____________")
    
response = input('Do you have an account with us? y/n ')

if response.lower() == 'n' or response.lower() == 'no':
    opening_an_account()
elif response.lower() == 'y' or response.lower() == 'yes':
    login()
else:
    print('invalid response')
        
print('\n\n\n')
print(datas)
print(datas_for_another_bank)


