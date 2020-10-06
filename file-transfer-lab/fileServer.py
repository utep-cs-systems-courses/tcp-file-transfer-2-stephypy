#!/usr/bin/env python3

"""
@author: Stephanie Galvan
@course: Theory of Operating Systems
@assignment: 2 - TCP File Transfer
@python-version: 3.7.0
"""
import os
import socket, sys

sys.path.append("../lib")  # for params
import params

HOST = "127.0.0.1"
PATH_FILES = "./ReceivedFiles"


def write_file(filename, byte, conn):
    # create file to write
    file_writer = open(filename, 'wb')

    # receive and write data
    i = 0
    data = ''
    while i < byte:
        data = conn.recv(1024)
        if not data:
            break
        i += len(data)

    file_writer.write(data)

    # close and inform user
    file_writer.close()
    print("file %s received" % filename)


def get_byte_size(conn):
    data_byte = conn.recv(1024)
    return data_byte.decode()


def server():
    switchesVarDefaults = (
        (('-l', '--listenPort'), 'listenPort', 50001),
        (('-d', '--debug'), "debug", False),  # boolean (set if present)
        (('-?', '--usage'), "usage", False),  # boolean (set if present)
    )

    paramMap = params.parseParams(switchesVarDefaults)
    debug, listenPort = paramMap['debug'], paramMap['listenPort']

    if paramMap['usage']:
        params.usage()

    bind_addr = (HOST, listenPort)

    # creating listening socket
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # associating socket with host and port number
    listen_socket.bind(bind_addr)

    # "makes" listening socket with max connection to 5
    listen_socket.listen(5)
    print("listening on: ", bind_addr)

    # connection and tuple for client address (host, port)
    conn, addr = listen_socket.accept()
    print("connection rec'd from", addr)

    # move to directory to receive files
    os.chdir(PATH_FILES)

    while True:
        # receive file name first
        data = conn.recv(1024)
        d = data.decode()

        # file byte size
        data_byte = get_byte_size(conn)

        # if filename was provided, write it
        if d:
            write_file(d, int(data_byte), conn)

        if not data:
            break
        conn.sendall(data)


if __name__ == "__main__":
    server()
