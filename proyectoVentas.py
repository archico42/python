import csv
import os

CLIENT_TABLE='.clients.csv'
CLIENT_SCHEMA = ['name','company','email','position']
clients = []


def _initialize_clients_from_storage():
	with open(CLIENT_TABLE,mode='r') as f:
		reader = csv.DictReader(f,fieldnames=CLIENT_SCHEMA)

		for row in reader:
			clients.append(row)


def _save_clients_to_storage():
	tmp_table_name = '{}.tmp'.format(CLIENT_TABLE)
	with open(tmp_table_name,mode='w') as f:
		writer = csv.DictWriter(f,fieldnames=CLIENT_SCHEMA)
		writer.writerows(clients)

	os.remove(CLIENT_TABLE)
	os.rename(tmp_table_name,CLIENT_TABLE)


def verifyNameClient(client):
    global clients
    
    if client in clients:
        return True
    else:
        return False


_clientNotFund_ = lambda: print('that name is not on the client list')


def insert_name(clients_name):
    global clients
    
    if verifyNameClient(clients_name):
        print('Client is already in the client\'s list')
        return clients
    else:
        clients.append(clients_name)   
        return clients
    

def viewLisClient():
    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid=idx,
            name = client['name'],
            company = client['company'],
            email = client['email'],
            position = client ['position']
            ))

def updateClient(client):
    global clients
    
    if verifyNameClient(client):
        indexList = clients.index(client)
        clients.remove(client)
        update_name = input('Give me the name of the client to update: ')
        update_company = input('Give me the company of the client to update: ')
        update_email = input('Give me the email of the client to update: ')
        update_position = input('Give me the position of the client to update: ')
        client['name'] = update_name
        client['company'] = update_company
        client['email'] = update_email
        client['position'] = update_position
        clients.insert(indexList, client)
    else:
        print('The client was not found.')

def deleteClient(client):
    global clients
    
    if verifyNameClient(client):
        clients.remove(client)
    else:
        _clientNotFund_()


def searchClient(client_name):
    for client in clients:
        if client['name'] != client_name:
            continue
        else:
            return True

def nameClient():
    while True:
        name = input('What is client\'s name: ')
        if len(name) > 0:
            return name

def _getClientfield(field_name):
    field = None
    
    while not field:
        field = input('What is the client {}?'.format(field_name))
        
        return field

def _welcomeProjectSell_():
    print('Welcome to project ventas')
    print('Choose an option')
    print('[A] Add client')
    print('[D] Delete client')
    print('[U] Update client')
    print('[S] Search client')
    
    
if __name__ == '__main__':
   	
    _initialize_clients_from_storage()

    _welcomeProjectSell_()
    
    command = input().upper()
    
    if command == 'A':
        client = {
            'name': _getClientfield('name'),
            'company': _getClientfield('company'),
            'email': _getClientfield('email'),
            'position': _getClientfield('position'),
                }
        insert_name(client)
        viewLisClient()
    elif command == 'U':
        client = {
            'name': _getClientfield('name'),
            'company': _getClientfield('company'),
            'email': _getClientfield('email'),
            'position': _getClientfield('position'),
                }
        updateClient(client)
        viewLisClient()
    elif command == 'D':
        client = {
            'name': _getClientfield('name'),
            'company': _getClientfield('company'),
            'email': _getClientfield('email'),
            'position': _getClientfield('position'),
                }
        deleteClient(client)
        viewLisClient()
    elif command == 'S':
        client_name = _getClientfield('name')
        found = searchClient(client_name)
        
        if found:
            print('The client is in the client\'s list')
        else:
            print('The client: {} is not in our client\'s list'.format(client_name))
    else:
        print('You chose an invalid option')

    _save_clients_to_storage()