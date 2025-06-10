import myparamiko
import getpass

# This script uses the already reated module myparamiko.py 
# and executes linux commands o a defined server

passwd =getpass.getpass("Enter the server password: ")

server= {'server_ip':'172.19.173.17', 'user':'nnikol', 'server_port':22,'passwd':passwd}
ssh_server = myparamiko.connect(**server)
shell = myparamiko1.get_shell(ssh_server)

result = myparamiko.exec_cmd(shell,'cd workspace')
print(result)
result = myparamiko.exec_cmd(shell,"pwd")
print(result)
result = myparamiko.exec_cmd(shell,'ls -la')
print(result)

myparamiko.close(ssh_server)
    
