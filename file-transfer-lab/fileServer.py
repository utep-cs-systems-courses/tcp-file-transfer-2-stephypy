#!/usr/bin/env python3

"""
@author: Stephanie Galvan
@course: Theory of Operating Systems
@assignment: 2 - TCP File Transfer
@python-version: 3.7.0
"""

import socket, sys

sys.path.append("../lib")  # for params
import params

HOST = "127.0.0.1"


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
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # associating socket with host and port number
        s.bind(bind_addr)

        # "makes" s listening socket
        s.listen()
        print("listening on: ", bind_addr)

        # connection and tuple for client address (host, port)
        conn, addr = s.accept()

        with conn:
            print("connection rec'd from", addr)
            data = conn.recv(1024)
            decoded_data = data.decode()
            while True:
                if not data:
                    break
                conn.sendall(data)


if __name__ == "__main__":
    server()
