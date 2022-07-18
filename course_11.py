import  uuid

ADD_CLIENT_COMMAND = 'add_client'
READ_CLIENT_BALANCE = 'read_balance'
HELP_COMMAND = 'help'
EXIT_COMMAND = 'exit'
IS_USER_LOGED_IN = False

def login(user, password):
    file = open('auth.txt', 'r')  # user,passwor
    for line in file:
        data = line.split(',')
        user_name = data[0]
        user_password = data[1]
        if user == user_name and password == user_password:
            file.close()
            return True
    file.close()
    return False


def must_login():
    global IS_USER_LOGED_IN
    print("You need to log in!")
    user_name = input('Please insert username: ')
    user_password = input('Please insert password: ')
    if login(user_name, user_password):
        IS_USER_LOGED_IN = True
        print("User has loged in!")
    else:
        print("Try again, uername/password incorrect!")

def start_create_user_procedure():
    print("Add new client")
    file = open('clients.txt', 'a')
    client_id = uuid.uuid4()
    client_name = input('Client name: ')
    client_phone = input('Client phone: ')
    client_town = input('Client town: ')
    file.write(f'{client_id},{client_name},{client_phone},{client_town} \n')
    file.close()

    file = open('accounts.txt', 'a')
    file.write(f'{client_id},{0},RON\n')
    file.close()

print('''
    Welcome to the Titulescu Bank!

    If you don't know hou to use the application please use the "help" command.
''')





while True:
    user_command = input('Please specify your command: ').lower()
    if user_command == EXIT_COMMAND:
        break
    elif user_command == HELP_COMMAND:
        print('''
        This application can do a multitude of things based on the command that was imputed.
        Commands available :
            - add_client Starts process for adding new client
            - exit To exist the application   
        ''')
    elif user_command == ADD_CLIENT_COMMAND:
        if IS_USER_LOGED_IN:
            start_create_user_procedure()
        else:
            must_login()
            start_create_user_procedure()
    elif user_command == READ_CLIENT_BALANCE:

        print("Specify clinet's information")
        client_name = input("Client name: ")
        client_phone = input("Client phone: ")
        file = open('clients.txt', 'r')
        client_id = None
        for line in file:
            client_data = line.split(',')
            client_data_name = client_data[1]
            client_data_phone = client_data[2]
            if client_name == client_data_name and client_phone == client_data_phone:
                client_id = client_data[0]
        file.close()
        if client_id:
            accounts_file = open('accounts.txt','r')
            all_acounts = accounts_file.readlines()
            for account in all_acounts:
                account_data = account.split(',')
                if client_id == account_data[0]:
                    print(f'Your account has {account_data[1]}{account_data[2]}')
        else:
            print('User does not exist in the system.')
