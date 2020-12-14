import os
def introductory_display():
    _ = os.system('clear')
    print('Welcome to the INVESTMENT ADVISOR EXPERT SYSTEM.')
    print('I will attempt to determine a portfolio investment for your client.')
    print('I will ask you both personal and financial questions about the client.')
    print('From this information, I should be able to determine either a conservative or an aggresive investment.')
    

def get_return():
    x = input('Please press RETURN to continue.')

def ask_amount():
    _ = os.system('clear')
    print("How much money in dollars does the client want to invest?")
    print("Please enter the dollar amount withou commas, e.g., 10000")

def ask_age():
    _ = os.system('clear')
    print("What is the client's age?")

def ask_service_length():
    _ = os.system('clear')
    print("How many years has the client been with the present company?")

def ask_layoffs():
    _ = os.system('clear')
    print("Layoffs at the organization are:")
    print('low')
    print('high')

def ask_children():
    _ = os.system('clear')
    print('The client has:')
    print('children')
    print('no children')

def get_assets():
    _ = os.system('clear')
    print('Please give the total dollar amount of assets that the clinet owns.')
    print('Include holdings in such items as bank accounts, stocks, bonds, real estate, etc.')
    print('Please enter the dollar amount without the commas, e.g., 150000.')

def get_liabilities():
    _ = os.system('clear')
    print('Please give the total dollar amount in liabilities that the client owes.')
    print('Include such items as loans, mortgages, etc.')
    print('Please enter the dollar amount without commas, e.g., 150000')

def ask_reset():
    x = input('To exit the system type \'e\'. If you would like to restart the session type \'r\': ')
    if(x == 'e'):
        return False
    elif(x == 'r'):
        return True
    else:
        return False

def is_old(old_age, client_age):
    if client_age < old_age:
        return False
    elif client_age >= old_age:
        return True

def is_job_steady(service_length, short_service, long_service, layoff):
    if service_length >= long_service:
        return True
    elif service_length < long_service and service_length >= short_service and layoff == 'low':
        return True
    elif service_length < long_service and service_length >= short_service and layoff == 'high':
        return False
    elif service_length < short_service:
        return False
    else:
        return None

def print_recommendation(portfolio):
    _ = os.system('clear')
    if portfolio == 1:
        print('Portfolio advice is 100percent investment in savings')
    elif portfolio == 2:
        print('Portfolio advice is 60percent stocks, 30percent bonds, 10percent savings')
    elif portfolio == 3:
        print('Portfolio advice is 20percent stocks, 40percent bonds, 40percent savings')
    elif portfolio == 4:
        print('Portfolio advice is 100percent investment in stocks')
    else:
        print('Portfolio advice is unknown')

def print_reason(personal_state, financial_state):
    print('The major reasons why I recommend this investment is that I found the client\'s personal state suggests a/an '+ personal_state + ' and financial state suggests a/an '+ financial_state)

# amount, client_age, service_length, layoff, children, total_liabilities, total_assets
flag = True
while flag:
    OLD_AGE = 40
    LONG_SERVICE = 10
    SHORT_SERVICE = 3
    SAFETY_FACTOR = 2
    introductory_display()
    get_return()
    ask_amount()
    amount = int(input(''))
    ask_age()
    client_age = int(input(''))
    ask_service_length()
    service_length = int(input(''))
    ask_layoffs()
    layoff = input('')
    ask_children()
    children = input('')

    # evaluation of personal state
    if is_old(OLD_AGE, client_age) or not is_job_steady(service_length, SHORT_SERVICE, LONG_SERVICE, layoff):
        personal_state = 'conservative'
    elif not is_old(OLD_AGE, client_age) and is_job_steady(service_length, SHORT_SERVICE, LONG_SERVICE, layoff) and children == 'children':
        personal_state = 'conservative'
    elif not is_old(OLD_AGE, client_age) and is_job_steady(service_length, SHORT_SERVICE, LONG_SERVICE, layoff) and children == 'no children':
        personal_state = 'aggressive'
    else:
        personal_state = 'unknown'
    print('After considering the client\'s personal issue, I would suggest a ' + personal_state + '. I will next look into the client\'s financial issue')

    get_return()
    get_assets()
    total_assets = int(input())
    get_liabilities()
    total_liabilities = int(input())
    
    # evaluation of financial state
    if total_assets < total_liabilities:
        financial_state = 'conservative'
    elif total_assets > total_liabilities and total_assets < SAFETY_FACTOR * total_liabilities and children == 'children':
        financial_state = 'conservative'
    elif total_assets > SAFETY_FACTOR * total_liabilities:
        financial_state = 'aggressive'
    elif total_assets > total_assets and total_assets < SAFETY_FACTOR * total_liabilities and children == 'no children':
        financial_state = 'aggressive'
    else:
        financial_state = 'unknown'

    get_return()
    
    # evaluation of recommendation
    if amount < 1000:
        portfolio = 1
    elif personal_state == 'conservative' and financial_state == 'conservative':
        portfolio = 1
    elif personal_state == 'conservative' and financial_state == 'aggressive':
        portfolio = 2
    elif personal_state == 'aggressive' and financial_state == 'conservative':
        portfolio = 3
    elif personal_state == 'aggressive' and financial_state == 'aggressive':
        portfolio = 4
    else:
        portfolio = 'unknown'
    print_recommendation(portfolio)

    # evaluation of reason
    print_reason(personal_state, financial_state)

    if(not ask_reset()):
        flag = False