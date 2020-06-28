import socket
import  threading

#for local host
Host='127.0.0.1'
# the port_no is optional you can choose any port_no but be free!
Port_no=45687
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((Host,Port_no))
#here we put the server on listening mode for listening the connection.
server.listen()
# if new client is joining the put into the client list and the name list used for the name of the client.
clients=[]
name=[]
# this function is broadcast function this function send the messege to all the client which is connected to this server.
def broadcast(msg):
    for client in clients:
        client.send(msg)
# here function is broadcast the messege to all the client that is connected to the server.
def handle_client(client):
    while 1:
        try:
            message=client.recv(1024) #1024 is file size it can be change by your need.
            broadcast(msg)
        except:
            index=clints.index(client)# in this block remove the client from the serverif any error occur and send there name of client which can be remove.
            clients.remove(client)
            client.close()
            name_=name[index]
            name.remove(name_)
            broadcast(f'{name_}is left'.encode('ascii'))
            break
# this is the main method recieve method to combine and the messege all all client.
def receive():
    while 1:
        #here the client and address of the client.
        client,address=server.accept()
        print(f'connected with this address{str(address)}')
        # here ask the name of the client.
        client.send('what is your name'.encode('ascii'))
        name_=client,recv(1024).decode('ascii')
        name.append(name_)
        clients.append(client)
        # send the message to the all chat this name has join the chat.
        print(f'Name of the client is {name_}.')
        broadcast(f'{name_}join the chat.'.encode('ascii'))
        client.send('you are join chat Room'.encode('ascii'))

        thread=threading.Thread(target=handle_client,args=(client,))
        thread.start()
print("server is listening....")
receive()
