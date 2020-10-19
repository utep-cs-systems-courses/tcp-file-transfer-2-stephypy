# File Transfer Lab (Forking)

##### author: Stephanie Galvan
##### python version: 3.7.0

## Description

The following lab implements a file transfer server with forking

## Features

* File transfer is done with forking
* Prevents users from sending empty files
* Overwrites files if a file is already in the `ReceivedFiles` directory
* Server can run with and without the proxy

## How To Run

### with steamer proxy

1. Run the proxy file by going to `stammer-proxy` directory and running `./stammerProxy.py` on the command line
2. On a separate cmd window, navigate to `file-transfer-lab` directory and run `./fileServer.py`
3. On a separate cmd window, navigate to `file-transfer-lab` directory and run `./fileClient.py`
4. To quit, enter `exit` on the window with `./fileClient.py` running
5. Otherwise, enter the filename (including its extension) on the command (i.e. `hello.txt`)

### without steamer proxy
1. On a separate cmd window, navigate to `file-transfer-lab` directory and run `./fileServer.py`
2. On a separate cmd window, navigate to `file-transfer-lab` directory and run `./fileClient.py`
3. To quit, enter `exit` on the window with `./fileClient.py` running
4. Otherwise, enter the filename (including its extension) on the command (i.e. `hello.txt`)