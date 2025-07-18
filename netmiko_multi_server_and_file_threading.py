from netmiko import ConnectHandler
from datetime import datetime
import threading

# This script can be used for multi server multi file configuration


def backup(server):
    
    now=datetime.now()
    year= now.year
    month=now.month
    day=now.day

    connection =ConnectHandler(**server)
    print(f"Connection on server {server['host']} ")

    file =input(f"Enter the file configuration for the server {server['host']}: ")
    print(f'Running commands from file: {file} on server: {["server"]}')
    output = connection.send_config_from_file(file)

    output_filename= f"logfile_{server}_file_{year}-{month}-{day}.txt"
    with open(output_filename, 'w') as o_f:
        o_f.write(output)

    print(f'Closing connection to {server["host"]}')
    connection.disconnect()


with open('devices.txt', 'r') as f:
    devices=f.read().splitlines()

threads =[]

for ip in devices: 
    server ={
        'host':ip,
        'username':'nnikol',
        'port':22,
        'password':'2011',
        'device_type':'linux',
        'verbose': True
        }
    th =threading.Thread(target=backup, args=server)
    threads.append(th)

for th in threads:
    th.start()

for th in threads:
    th.join() 