#!/usr/bin/env python3


import time
import base64
import paramiko


_host = "ptt.cc"
_user = "bbsu"
_pass = ""

_ptt_username = "Your Ptt username"
_ptt_passwd = "Your Ptt password"

client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname = _host, username = _user, password = _pass)

chan = client.invoke_shell()

# Ptt welcome page
chan.recv(9999).decode('big5')
time.sleep(3)

# Enter username
chan.send(_ptt_username + "\r\n")
chan.recv(9999).decode()
time.sleep(3)

# Enter password
chan.send(_ptt_passwd + "\r\n")
chan.recv(9999).decode()
time.sleep(3)

# Input enter for passing bridge page
chan.send("\r\n")
chan.recv(9999).decode()
time.sleep(3)

# Show the board page
chan.recv(9999).decode()
time.sleep(3)

# Enter test board
chan.send("s")
chan.send("test\r\n")
time.sleep(3)
chan.recv(9999).decode()
chan.send("\r\n")
chan.recv(9999).decode()

# Post test article in test board
chan.send("\x10") # Enter post page
chan.recv(9999).decode()
time.sleep(3)
chan.send("1\r\n") # Article type
chan.recv(9999).decode()
time.sleep(3)
chan.send("Test\r\n") # Title
chan.recv(9999).decode()
time.sleep(3)
chan.send("Test") # Content
chan.recv(9999).decode()
time.sleep(3)
chan.send("\x18")
chan.recv(9999).decode()
time.sleep(3)
chan.send("s\r\n") # Save article
chan.recv(9999).decode()
time.sleep(3)
chan.send("\r\n") # Save article
chan.recv(9999).decode()
time.sleep(3)

# Leave Ptt
chan.send("\x1b[D")
chan.recv(9999).decode()
time.sleep(3)
chan.send("\x1b[D")
chan.recv(9999).decode()
time.sleep(3)
chan.send("\r\n")
chan.recv(9999).decode()
time.sleep(3)
chan.send("y\r\n")
chan.recv(9999).decode()
time.sleep(3)
chan.send("\r\n")
chan.recv(9999).decode()
time.sleep(3)
