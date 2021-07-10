#!/usr/bin/env python3

import time
import base64
import paramiko

_output_mode = False

_host = "ptt.cc"
_user = "bbsu"
_pass = ""
_key_file = "Your SSH private key path"

_ptt_username = "Your Ptt username"
_ptt_passwd = "Your Ptt password"


def interact(chan, content):
    for c in content:
        if c is not None:
            chan.send(c)
            time.sleep(3)
        else:
            resp = chan.recv(9999)
            time.sleep(3)

        if _output_mode and c is None:
            try:
                print(resp.decode('utf-8'))
            except UnicodeDecodeError:
                print(resp.decode('big5'))


def main():
    client = paramiko.SSHClient()
    client.load_host_keys(_key_file)
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname = _host, username = _user, password = _pass)

    chan = client.invoke_shell()

    # Ptt welcome page
    interact(chan, [None])

    # Enter username
    interact(chan, [_ptt_username + '\r\n', None])

    # Enter password
    interact(chan, [_ptt_passwd + '\r\n', None])

    # Input enter for passing bridge page
    interact(chan, ['\r\n', None])

    # Enter test board
    interact(chan, ['s', 'test\r\n', None, '\r\n', None])

    # Post test article in test board
    interact(chan, ['\x10', None])  # Enter post page
    interact(chan, ['1\r\n', None])  # Article type
    interact(chan, ['Test\r\n', None])  # Title
    interact(chan, ['Test\r\n', None])  # Content
    interact(chan, ['\x18', None])
    interact(chan, ['s\r\n', None, '\r\n', None])  # Save article

    # Leave Ptt
    interact(chan, ['\x1b[D', None, '\x1b[D', None, '\r\n', None, 'y\r\n', None, '\r\n', None])


if __name__ == '__main__':
    main()
