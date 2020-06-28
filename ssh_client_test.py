#!/usr/bin/env python3

import time
import base64
import paramiko

_host = "ptt.cc"
_user = "bbsu"
_pass = ""                          # Keep it empty, this is not your Ptt password
_key_file = "Your SSHKey file path" # e.g., /home/AutoLogin/.ssh/id_rsa

_ptt_username = "Your Ptt username"
_ptt_passwd = "Your Ptt password"

client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname = _host, username = _user, password = _pass, key_filename = _key_file)

chan = client.invoke_shell()

# This part is the hidden part not displayed for normal usage, it shows the IP of the remote end
# It is encoded through big5, thus if you want to check the content, print it with big5 codec
chan.recv(9999)

# Ptt welcome page
print(chan.recv(9999).decode())
print(chan.recv(9999).decode())
time.sleep(3)

# Enter username
chan.send(_ptt_username + "\r\n")
print(chan.recv(9999).decode())
time.sleep(3)

# Enter password
chan.send(_ptt_passwd + "\r\n")
print(chan.recv(9999).decode())
time.sleep(3)

# Input enter for passing bridge page
chan.send("\r\n")
print(chan.recv(9999).decode())
time.sleep(3)

# Show the board page
print(chan.recv(9999).decode())
time.sleep(3)

# Enter test board
chan.send("s")
chan.send("test\r\n")
time.sleep(3)
print(chan.recv(9999).decode())
chan.send("\r\n")
print(chan.recv(9999).decode())

# Post test article in test board
chan.send("\x10") # Enter post page
print(chan.recv(9999).decode())
time.sleep(3)
chan.send("1\r\n") # Article type
print(chan.recv(9999).decode())
time.sleep(3)
chan.send("Test\r\n") # Title
print(chan.recv(9999).decode())
time.sleep(3)
chan.send("Test") # Content
print(chan.recv(9999).decode())
time.sleep(3)
chan.send("\x18")
print(chan.recv(9999).decode())
time.sleep(3)
chan.send("s\r\n") # Save article
print(chan.recv(9999).decode())
time.sleep(3)
chan.send("\r\n") # Save article
print(chan.recv(9999).decode())
time.sleep(3)

# Leave Ptt
chan.send("\x1b[D")
print(chan.recv(9999).decode())
time.sleep(3)
chan.send("\x1b[D")
print(chan.recv(9999).decode())
time.sleep(3)
chan.send("\r\n")
print(chan.recv(9999).decode())
time.sleep(3)
chan.send("y\r\n")
print(chan.recv(9999).decode())
time.sleep(3)
chan.send("\r\n")
print(chan.recv(9999).decode())
time.sleep(3)
