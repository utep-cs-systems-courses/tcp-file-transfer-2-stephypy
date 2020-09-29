#!/usr/bin/env python3

import socket, sys, re

sys.path.append("../lib")  # for params
import params


def client():
    switchesVarDefaults = (
        (('-s', '--server'), 'server', "127.0.0.1:50001"),
        (('-d', '--debug'), "debug", False),  # boolean (set if present)
        (('-?', '--usage'), "usage", False),  # boolean (set if present)
    )

    paramMap = params.parseParams(switchesVarDefaults)

    server, usage, debug = paramMap["server"], paramMap["usage"], paramMap["debug"]

    if usage:
        params.usage()

    try:
        serverHost, serverPort = re.split(":", server)
        serverPort = int(serverPort)
    except:
        print("Can't parse server:port from '%s'" % server)
        sys.exit(1)

    addr_port = (serverHost, serverPort)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(addr_port)

        while True:
            filename = input("> ")
            if filename == "exit":
                sys.exit(0)
            else:
                s.sendall(filename.encode())
                data = s.recv(1024)
                print('Received', repr(data))


if __name__ == "__main__":
    client()
