import socket
import threading

# Lista dei client connessi
clients = []
aliases = []

# Funzione per gestire i messaggi ricevuti da un client
def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message, client)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            alias = aliases[index]
            broadcast(f'{alias} has left the chat!'.encode('utf-8'), client)
            aliases.remove(alias)
            break

# Funzione per inviare un messaggio a tutti i client
def broadcast(message, client):
    for c in clients:
        if c != client:
            c.send(message)

# Funzione principale per iniziare il server
def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 5555))
    server.listen()

    print('Server is listening...')

    while True:
        client, address = server.accept()
        print(f'Connection from {address}')

        client.send('NICK'.encode('utf-8'))
        alias = client.recv(1024).decode('utf-8')
        aliases.append(alias)
        clients.append(client)

        print(f'Nickname of the client is {alias}')
        broadcast(f'{alias} has joined the chat!'.encode('utf-8'), client)
        client.send('You are now connected!'.encode('utf-8'))

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

if __name__ == "__main__":
    main()
