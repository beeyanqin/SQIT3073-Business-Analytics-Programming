import functions as ft

def main():
    print('Welcome to Malaysian Tax Input Program')

    while True:
        user = input('Are you a new user? (Y --> yes, N --> No, X --> Exit): ')
        if user not in ['Y', 'y', 'N', 'n', 'X', 'x']:
            print('Invalid input. Please enter Y/N/X')
            continue
        if user in ['Y', 'y']:
            if not new_user():
                continue
            else:
                break
        elif user in ['N', 'n']:
            if not existing_user():
                continue
            else:
                break
        else:            
            break
    print('Thanks for visiting Tax Input Program')

def new_user():
    print('Please create an account')
    while True: 
        user_id = input('Enter your user ID: ')  
        if not ft.check_id(user_id):
            print('Invalid input. Should contain at least one uppercase, one digit and one symbol')
            continue

        while True:
            user_ic = input('Enter your IC: ')
            password = input('Enter your password (last 4 digit of IC): ')
            if not ft.verify_user(user_ic, password):
                print('IC should in 12 digits. Password is last 4 digits of IC')
                continue
            
            if ft.ic_exists(user_ic, 'user.csv'):
                print('This IC already registered')
                return False

            print('Account registered successfully')
            user_data = {'User ID' : user_id,
                         'User IC' : user_ic,
                         'Password' : password,
                         'Annual Income' : 0.00,
                         'Tax Relief' : 0.00,
                         'Tax Payable' : 0.00
                         }
            ft.save_to_csv(user_data, 'user.csv')
            print('Data save successfully')
            break
        information(user_ic)
        return True

def existing_user():
    user_id = input('Enter your id: ')
    password = input('Enter your password (last 4 digit of IC): ')
    if ft.read_from_csv(user_id, password, 'user.csv'):
        print('Login successful')
        user_ic = ft.get_user_ic(user_id, password)
        information(user_ic)
        return True
    else:
        print('User ID or password is invalid')
        return False

def information(user_ic):
    annual_income = float(input('Enter your annual income: '))
    tax_relief_amount = float(input('Enter the amount of tax relief: '))
    tax_payable = ft.calculate_tax(annual_income, tax_relief_amount)
    print('Tax payable: RM {:.2f}'.format(tax_payable))
    ft.update_user_data(user_ic, annual_income, tax_relief_amount, tax_payable, 'user.csv')

if __name__== "__main__":
    main()