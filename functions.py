import pandas as pd
import os
        
def check_id(user_id):
    has_upper = any(char.isupper() for char in user_id)
    has_digit = any(char.isdigit() for char in user_id)
    has_symbol = any(char in "!@#$%^&*()-_+=:;',<>./?" for char in user_id)
    return has_upper and has_digit and has_symbol

def verify_user(user_ic, password):
    if (len(user_ic) == 12) and (password == user_ic[8:12]):
        return True
    
def ic_exists(user_ic, user):
    try:
        if os.path.isfile(user):
            df = pd.read_csv(user, dtype={'User IC': str, 'Password': str})
            return user_ic in df['User IC'].values
        return False
    except:
        print('Error checking IC')

def save_to_csv(user_data, user):
    df = pd.DataFrame([user_data])
    header = not os.path.isfile(user)
    try:   
        df.to_csv (user, mode = 'a', header = header , index = False)
    except Exception as e:
        print(f'Error saving to csv: {e}')

def read_from_csv(user_id, password, user):
    if os.path.isfile(user):
        df = pd.read_csv(user, dtype={'User IC': str, 'Password': str})
        return ((df['User ID'] == user_id) & (df['Password'] == str(password))).any()
    else:
        return False
    
def get_user_ic(user_id, password):
    try:
        df = pd.read_csv('user.csv', dtype={'User IC': str, 'Password': str})
        user = df[(df['User ID'] == user_id) & (df['Password'] == str(password))]
        if not user.empty:
            return user.iloc[0]['User IC']
    except:
        print('Error getting user IC')

def calculate_tax(annual_income, tax_relief):
    taxable_income = float(annual_income) - float(tax_relief)
    if taxable_income <= 5000:
        return 0
    elif taxable_income <= 20000:
        return (taxable_income - 5000) * 0.01
    elif taxable_income <= 35000:
        return (15000 * 0.01) + ((taxable_income - 20000) * 0.03)
    elif taxable_income <= 50000:
        return (15000 * 0.01) + (15000 * 0.03) + ((taxable_income - 35000) * 0.06)
    elif taxable_income <= 70000:
        return (15000 * 0.01) + (15000 * 0.03) + (15000 * 0.06) + ((taxable_income - 50000) * 0.11)
    elif taxable_income <= 100000:
        return (15000 * 0.01) + (15000 * 0.03) + (15000 * 0.06) + (20000 * 0.11) + ((taxable_income - 70000) * 0.19)
    elif taxable_income <= 400000:
        return (15000 * 0.01) + (15000 * 0.03) + (15000 * 0.06) + (20000 * 0.11) + (300000 * 0.19) + ((taxable_income - 100000) * 0.25)
    elif taxable_income <= 600000:
        return (15000 * 0.01) + (15000 * 0.03) + (15000 * 0.06) + (20000 * 0.11) + (300000 * 0.19) + (300000 * 0.25) + ((taxable_income - 400000) * 0.26)
    elif taxable_income <= 2000000:
        return (15000 * 0.01) + (15000 * 0.03) + (15000 * 0.06) + (20000 * 0.11) + (300000 * 0.19) + (300000 * 0.25) + (200000 * 0.26) + ((taxable_income - 600000) * 0.28)
    else:
        return (15000 * 0.01) + (15000 * 0.03) + (15000 * 0.06) + (20000 * 0.11) + (300000 * 0.19) + (300000 * 0.25) + (200000 * 0.26) + (1400000 * 0.28) + ((taxable_income - 2000000) * 0.30)

def update_user_data(user_ic, annual_income, tax_relief, tax_payable, user):
    try:
        if os.path.isfile(user):
            df = pd.read_csv(user, dtype={'User IC': str, 'Password': str})
            df['Annual Income'] = df['Annual Income'].astype(float)
            df['Tax Relief'] = df['Tax Relief'].astype(float)
            df['Tax Payable'] = df['Tax Payable'].astype(float)
            df.loc[df['User IC'] == user_ic, 'Annual Income'] = float(annual_income)
            df.loc[df['User IC'] == user_ic, 'Tax Relief'] = float(tax_relief)
            df.loc[df['User IC'] == user_ic, 'Tax Payable'] = float(tax_payable)
            df.to_csv(user, index=False)
        else:
            print('Error: User does not exist')
    except:
        print('Error updating user data')
    