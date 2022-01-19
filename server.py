#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： LiuYuZhao
# datetime： 2022/1/17 19:15


import socket
import select

# define user name and password
# format is (user name, password)
password = [(123, 456), (123456, 123456)]
name = []
passw = []
for i, j in password:
    name.append(i)
    passw.append(j)

def main():
    serverIp = ''
    serverPort = 2022

    tcpSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpSock.bind((serverIp, serverPort))
    tcpSock.listen(5)

    inputs = [tcpSock]
    print('Server start ')
    print('Port ' + str(serverPort) + ' is listening ...\n')
    while True:
        rs, ws, es = select.select(inputs, [], [])
        for r in rs:
            # judge weather start connect
            if r is tcpSock:
                cli, addr = tcpSock.accept()
                connInfo = 'User ' + str(addr) + ' is connected'
                print(connInfo)
                inputs.append(cli)
                for sock in inputs:
                    if sock is tcpSock:
                        continue
                    if sock is cli:
                        sock.send('Welcome to server'.encode('utf-8'))
                        continue
                    # sock.send(connInfo.encode('utf-8'))

            else:
                try:
                    # receive data
                    data = r.recv(1024)
                    disconnected = not data
                except socket.error:
                    disconnected = True

                if disconnected:
                    disconnInfo = 'User ' + \
                                  str(r) + 'is disconnected'
                    print(disconnInfo)
                    print('\n')
                    inputs.remove(r)

                else:
                    try:
                        recvInfo = str(r.getpeername()) + \
                                   ': ' + data.decode('utf-8')
                        usr_name, passwd = data.decode('utf-8').split('&')
                    except UnicodeDecodeError as err:
                        print("Unicode Decode Error {0}".format(err))
                    except:
                        raise

                    print(recvInfo)
                    print(usr_name)
                    print(passwd)

                    # judge weather in password list
                    for u, p in password:
                        if str(u) == str(usr_name) and str(p) == str(passwd):
                            print("password direct")
                            # if true send True to client
                            sock.send("True".encode('utf-8'))
                            break
                        elif (str(u) == str(usr_name) and str(p) != str(passwd)) or (str(u) != str(usr_name) and str(p) == str(passwd)) or (str(u) != str(usr_name) and str(p) != str(passwd)):
                            print("password error")
                            # if false send False to client
                            sock.send("False".encode('utf-8'))
                    print()
                    for sock in inputs:
                        if sock is tcpSock:
                            continue
    tcpSock.close()


if __name__ == '__main__':
    main()
