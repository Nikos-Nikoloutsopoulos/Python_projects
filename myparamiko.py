import paramiko
import time
import getpass

def connect(server_ip, user, server_port, passwd):
    ssh_client=paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print(f"Connecting to {server_ip}")
    ssh_client.connect(hostname=server_ip, username = user, port = server_port, password = passwd, look_for_keys=False, allow_agent=False)
    return ssh_client

def get_shell(ssh_client):
    shell = ssh_client.invoke_shell()
    return shell

def exec_cmd(shell, command, timeout=1):
    print(f'Sending command: {command}')
    shell.send(command + '\n')
    time.sleep(timeout)
    output = shell.recv(10000).decode()
    return output

def close(ssh_client):
    if ssh_client.get_transport().is_active() ==True:
        print("Closing connection")
        ssh_client.close()

