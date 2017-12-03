# chat_server.py

import sys, socket, select
HOST = ''
SOCKET_LIST = []
RECV_BUFFER = 4096
try:
        PORT = int(sys.argv[1])
except:
        print('use command : python server.py PORT')
        exit(1)
chat_list=['Varanasi','IIT_BHU','Hostel','Important_@info']
clients_file=dict()
users=dict()
def chat_server():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(10)

    # add server socket object to the list of readable connections
    SOCKET_LIST.append(server_socket)

    print ("Chat server started on port"+ str(PORT))

    while 1:
        # get the list sockets which are ready to be read through select
        # 4th arg, time_out  = 0 : poll and never block
        ready_to_read,ready_to_write,in_error = select.select(SOCKET_LIST,[],[],0)
        for sock in ready_to_read:

            # a new connection request recieved
            if sock == server_socket:
                sockfd, addr = server_socket.accept()
                SOCKET_LIST.append(sockfd)
                print ("Client (%s, %s) connected" % addr)
                sockfd.send('\nWelcome to Our Server[15075028]....\nEnter Chat Option[1-4]\n1.Varansi\n2.IIT BHU\n3.Hostel\n4.Important @info\n\n')
                try:
                        while 1:
                                data=sockfd.recv(RECV_BUFFER)
                                try:
                                        int(data)
                                except:
                                        sockfd.send('Enter Integer Value ....\n')
                                        continue
                                if int(data) in range(1,5):
                                        sockfd.send('\nYou are Successfully Connected To chat option '+chat_list[int(data)-1]+'\nEnter User Name for Chat:\n')
                                        datau=sockfd.recv(RECV_BUFFER)
                                        sockfd.send('\nconnectd users are '+str(list(users.values()))+' ...\n')
                                        users[sockfd]=datau.strip()
                                        clients_file[sockfd]=chat_list[int(data)-1]
                                        file=open(clients_file[sockfd],'ab')
                                        file.close()
                                        break
                                else:
                                        sockfd.send('\nEnter Correct option[1-4]\n')
                except:
                        pass
                try:
                        broadcast(server_socket, sockfd, str(addr)+" "+users[sockfd].strip()+": "+" Entered our chatting room\n")
                except:
                        broadcast(server_socket, sockfd, "[%s:%s] Entered our chatting room\n" % addr)

            # a message from a client, not a new connection
            else:
                # process data recieved from client,
                try:
                    # receiving data from the socket.
                    data= sock.recv(RECV_BUFFER)
                    if data:
                        # there is something in the socket
                        data=data.strip()

                        if data[::-1][:4]!='sih@':
                                file=open(clients_file[sock],'ab')
                                file.write(str(addr)+' '+str(users[sock]).strip()+': '+data+'\n')
                                file.close()
                        try:
                                broadcast(server_socket, sock, "\r" + '[' + str(sock.getpeername()) + '] '+users[sock]+': '+ data)
                        except:
                                broadcast(server_socket, sock, "\r" + '[' + str(sock.getpeername()) + '] '+ data)
                    else:
                        # remove the socket that's broken
                        if sock in SOCKET_LIST:
                            SOCKET_LIST.remove(sock)
                            del users[sock]
                            del clients_file[sock]

                        # at this stage, no data means probably the connection has been broken
                        try:
                            print(addr,' is offline')
                            broadcast(server_socket, sock, 'Client '+str(addr)+' '+users[sock].strip()+' is offline\n')
                        except:
                            print(addr,' is offline')
                            broadcast(server_socket, sock, 'Client '+str(addr)+' is offline\n')

                # exception
                except:
                    try:
                        broadcast(server_socket, sock, 'Client '+str(addr)+' '+users[sock].strip()+' is offline\n')
                    except:
                        broadcast(server_socket, sock, 'Client '+str(addr)+' is offline\n')
                    continue

    server_socket.close()

# broadcast chat messages to all connected clients
def broadcast (server_socket, sock, message):
    for socket in SOCKET_LIST:
        # send the message only to peer
        message=message.strip()
        if socket != server_socket:
            try :
                if message[::-1][:4]=='sih@':
                    message='\n'+open(clients_file[sock],'rb').read()
                    if message:
                        sock.send(message+'\n')
                    else:
                        sock.send('Sorry History is not avialable for this chat...\n')
                    break
                elif socket!=sock:
                    socket.send(message+'\n')
            except :
                # broken socket connection
                socket.close()
                # broken socket, remove it
                if socket in SOCKET_LIST:
                    SOCKET_LIST.remove(socket)

if __name__ == "__main__":

    sys.exit(chat_server())
