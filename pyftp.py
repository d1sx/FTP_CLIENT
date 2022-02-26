#!/bin/python3

from ftplib import FTP
from os import system
import sys
r = '\033[1;31m'
b = '\033[1;34m'
w = '\033[1;97m'
g = '\033[1;32m'
c = '\033[1;36m'
try:
    IP = sys.argv[1]
    USER = str(sys.argv[2])
    PASS = str(sys.argv[3])
except:
    print(f'{r}Error\n\tUse: \t python3', sys.argv[0], '{ip_address} {username} {password}'); exit()
try:
    ftp = FTP()
    ftp.connect(IP, 21)
    ftp.login(USER, PASS)
    print(f'{c}[{g}ok{c}] - {c} connected to host')
    ftp.getwelcome()
except:
    print(f'{r}[error] - failed to connect to host! '); exit()
while True:
    cmd = str(input(f'{c}FTP> {b}'))
    if cmd.lower() == 'help':
        print(f'''{b}

        ls                    | list files and directory.
        pwd                   | show current directory.
        quit                  | exit.
        put      [local_file] | upload file.
        cd       [path]       | enter directory.
        get      [file]       | download files.
        mkdir    [path_name]  | make directory.
        rmdir    [path]       | remove directory.
        rmfile   [file]       | remove files.
        
        ''')
        
    elif cmd.lower() == 'ls':
        ftp.retrlines('LIST')
    elif 'rmdir' in cmd or 'RMDIR' in cmd and cmd.split() > 1:
        try:
            ftp.rmd(f'{cmd.split()[1]}')
        except:
            print(f'{r}[ error ] - permission denied, you do not have delete permission')
    elif cmd.lower() == 'quit':
        ftp.quit(); print(f'{c}221 Goodbye.'); exit()
    elif cmd.lower() == 'clear':
        system('clear')

    elif 'put' in cmd or 'PUT' in cmd and cmd.split() > 1:
        try:
            file = open(f'{cmd.split()[1]}','rb')
        except:
            print(f'{r}[ error ] - File not found ')
        try:
            ftp.storbinary(f'STOR {cmd.split()[1]}', file)
            print(f'{c}[{g}ok{c}] - file uploaded successfully!'); file.close()
        except:
            print(f'{r}[ error ] - permission denied, you do not have write permission')
    elif 'rmfile' in cmd or 'RMFILE' in cmd and cmd.split() > 1:
        try:
            ftp.delete(f'{cmd.split()[1]}')
        except:
            print(f'{r}[ error ] - permission denied, you do not have delete permission')
    elif cmd.lower() == 'pwd':
        print(ftp.pwd())
    elif 'mkdir' in cmd or 'MKDIR' in cmd and cmd.split() > 1: 
        try:
            ftp.mkd(f'{cmd.split()[1]}'); print(f'{c}[{g}ok{c}]{g} -{c} folder {b}{cmd.split()[1]}{c}created successfully!')
        except:
            print(f'{r}[ error ] - permission denied, you do not have write permission')
    elif 'cd' in cmd or 'CD' in cmd:
        ftp.cwd(cmd.split()[1])
    elif 'get' in cmd or 'GET' in cmd:
        file = open(f'{cmd.split()[1]}', 'wb')
        try:
            ftp.retrbinary(f'RETR {cmd.split()[1]}', file.write); file.close()
            print(f'{c}[{g}ok{c}] - file installed successfully', ftp.size(cmd.split()[1]))
        except:
            print(f'{r}[ error ] - File {b}{cmd.split()[1]}{r} not found..')
            system(f'rm -rf {cmd.split()[1]}')
    else:
        print(f'{r}[ error ] - command not fund! use [ {b}help{r} ] to view commands')

# --{*********}-- #
# author: d1sx    #
# date 27/01/2022 #
# --{*********}-- #
