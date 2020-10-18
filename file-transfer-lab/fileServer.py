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
from framedSock import framedSend, framedReceive

HOST = "127.0.0.1"
PATH_FILES = "./ReceivedFiles"
CONFIRM_MSG = "file %s received from %s"


def write_file(filename, file_content, conn, addr):
    try:
        # create file to write
        file_writer = open(filename, 'w+b')
        file_writer.write(file_content)

        # close and print confirmation msg on server
        file_writer.close()
        print(CONFIRM_MSG % (filename, addr))
    except FileNotFoundError:
        print("ERROR: file %s not found " % filename)
        # send failed status
        conn.sendall(str(0).encode())
        sys.exit(1)


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

    # move to directory to receive files
    os.chdir(PATH_FILES)

    while True:
        # connection and tuple for client address (host, port)
        conn, addr = listen_socket.accept()

        # check connection and client address exist otherwise exit
        if not conn or not addr:
            sys.exit(1)

        if not os.fork():
            print("connection rec'd from", addr)

            try:
                # receiving files sent from client
                filename, file_content = framedReceive(conn, debug)
            except:
                print("ERROR: file transfer failed")
                # send failed status
                conn.sendall(str(0).encode())
                sys.exit(1)

            # attempt to save files into ReceivedFiles folder
            filename = filename.decode()
            write_file(filename, file_content, conn, addr)

            # send success status
            conn.sendall(str(1).encode())
            sys.exit(0)


if __name__ == "__main__":
    server()
