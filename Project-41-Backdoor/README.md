### It a python based project called as Backdoor.


Backdoors are used for accessing file system of victim's machine connected over the same network.

Before testing this backdoor on your machine(s), make sure that both the devices are connected on same network.
Inorder to use/test this:
1. Modify the values in address.py and set the IP_ADDR(IP address) of your host machine and give the PORT number of your choice.
2. Run listener.py on host machine to start recieving connection.
3. Run reverse_backdoor.py on victim's machine and establish the connection between host and victim.
4. Once the connection is established, you can execute system commands of victim's machine from your host machine. 
