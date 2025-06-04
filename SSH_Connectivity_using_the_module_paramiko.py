import paramiko
import time
import getpass

# This utility can be used for ssh remote server connectivity.
# After that using the module paramiko, Linux commands can be run on different the remote servers


ssh_server =paramiko.SSHClient()

ssh_server.set_missing_host_key_policy(paramiko.AutoAddPolicy())

password = getpass.getpass("Enter the servers password: ")

server1 ={'hostname':'172.19.173.17','port':'22', 'username':'nnikol', 'password':password}
server2 ={'hostname':'172.19.173.18','port':'22', 'username':'nnikol', 'password':password}
server3 ={'hostname':'172.19.173.19','port':'22', 'username':'nnikol', 'password':password}

servers= [server1,server2,server3]

for server in servers:
    print(f"Connection to {server['hostname']}")
    ssh_server.connect(**server, look_for_keys=False, allow_agent=False)

    shell=ssh_server.invoke_shell()
    shell.send('cat /etc/rsyslog.conf \n')
    shell.send('ip route \n')
    shell.send('ls -la \n')
    shell.send('pwd \n')
    shell.send('ls -la | grep data > file.txt \n')
    shell.send('cd workspace/Ansible/diveintoansible-lab \n')
    shell.send('docker compose up \n')

    time.sleep(1)

    output = shell.recv(10000)
    output =output.decode('utf-8')
    print(output)

    if ssh_server.get_transport().is_active() ==True:
        print("Closing connection")
        ssh_server.close()