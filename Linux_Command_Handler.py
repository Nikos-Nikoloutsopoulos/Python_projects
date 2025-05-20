# This program reads linux commands from a commands.txt file.
# Executes the command on linux and store the output in the logfile.txt

import subprocess

with open ('commands.txt','+r') as input_file:
    data=input_file.readlines()

with open('logfile.txt','+w') as output_file:


    subprocess.run('clear')
    for command in data:
        print("---------------------------------------------------")
        print_file ="---------------------------------------------------\n" 
        output_file.writelines(print_file)
        print("Excuted the command: ", command)
        print_file = "Executed the command: " + command
        output_file.writelines(print_file)

        s1 = subprocess.run(command, capture_output=True, shell=True, text=True)
        if s1.returncode == 0:
            print("Successful printout")
            print_file ="Successful printout\n"
            output_file.writelines(print_file)
            print(s1.stdout)
            print_file = s1.stdout
            output_file.writelines(print_file)
        else:
            print("Unsuccessful printout")
            print_file ="Unsuccessful printout\n"
            output_file.writelines(print_file)
            print(s1.stderr)
            print_file = s1.stderr
            output_file.writelines(print_file)

output_file.close()
input_file.close()

