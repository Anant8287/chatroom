import socket
import threading
name_=input("Enter your name=")
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',45687))
# recieve all the time data from the server.
def receive():
    while 1:
        try:
            msg=client.recv(1024).decode('ascii')
            if message == 'what is your name':
                client.send(name_.encode('ascii'))

            else:
                print(msg)
        except:
            print("An error occurred !")
            client.close()
            break
def write():
    while 1:
        msg=f'{name_}:{input("")}'
        client.send(msg.encode('ascii'))
receive_thread=threading.Thread(target=receive)
receive_thread.start()
write_thread=threading.Thread(target=write)
write_thread.start()
