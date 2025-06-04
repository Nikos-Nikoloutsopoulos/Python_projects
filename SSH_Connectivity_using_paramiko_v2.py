import paramiko
import time
import getpass

def std_output(cmd):
    stdin, stdout, stderr = ssh_server.exec_command(cmd)
    output = stdout.read().decode()
    print(output) 
    output = stderr.read().decode() 

    return output
    
ssh_server=paramiko.SSHClient()

ssh_server.set_missing_host_key_policy(paramiko.AutoAddPolicy())
password =getpass.getpass("Enter the server password: ")

server= {'hostname':'172.19.173.17', 'port':22, 'username':'nnikol','password':password}
print(f"Connection to {server['hostname']}")
ssh_server.connect(**server, look_for_keys=False, allow_agent=False)

with open('cmd_input.txt','r') as f:
    cmds = f.readlines()
    print(cmds)
    for cmd in cmds:
        time.sleep(1)
        print(std_output(cmd))

if ssh_server.get_transport().is_active() ==True:
    print("Closing connection")
    ssh_server.close()
