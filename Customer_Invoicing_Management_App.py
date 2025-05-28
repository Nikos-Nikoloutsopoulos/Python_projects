import os
# CUSTOMER INVOICING MANAGEMENT APPLICATION

# This project requests from user to create or reuse a folder in which will 
# be stored the customer files.
# Each customer file can be used for storing or removing invoicing data.
# The user can delete a customer file


os.system('cls')
print("Create or reuse a directory for storing the customer files. ")
user_dir=input("Enter the user directory: ")

os.makedirs(user_dir,exist_ok=True)

while True:
    user_input = int(input(f" 1) Create a customer file with the related header \n 2) Choose a customer file and append new invoicing \n 3) Choose a customer file and delete an existing invoicing \n 4) Detele an existing customer file \n 5) EXIT \n Enter your choice: "))

    if user_input ==1: # Create a customer file with the related header
        os.system('cls')
        file_name=input("Create a new or reuse a customer file with name:  ")
        header = input("Insert the header in the customer file: ")
        path_name=os.path.join(user_dir,f"{file_name}.txt")
        with open(path_name,'w') as file:
            file.write(header + '\n')
    elif user_input ==2: # Choose a customer file and append new invoicing
        os.system('cls')
        print("The availible custome files are: \n")
        files=os.listdir(user_dir)
        for file in files:
            print(file)
        file_name=input("Which customer file will be used to add invoiceing: ")
        customer_name= input("Enter the new invoiceing name: ")
        customer_invoice= input("Enter the current invoicing amount: ")
        path_name=os.path.join(user_dir,f"{file_name}.txt")
        with open(path_name, 'a') as file:
            file.write(f"{customer_name}, {customer_invoice} \n")
        os.system('cls')
    elif user_input ==3: # Choose a customer file and delete an existing invoicing
        os.system('cls')
        print("The availible custome files are: \n")
        files=os.listdir(user_dir)
        for file in files:
            print(file)
        file_name=input("Which customer file will be used to remove invoicing: ")
        path_name=os.path.join(user_dir,f"{file_name}.txt")
        with open(path_name, 'r+') as file:
            os.system('cls')
            lines = file.readlines()
            for i, line in enumerate(lines):
                print(f"{i+1}) {line}", end="")
                
            try:
                user_input=int(input("Which line to delete: "))
            except ValueError:
                os.system('cls')
                print("Incorect Value")
                
            lines.pop(user_input -1)
            file.seek(0)
            file.truncate()
            file.writelines(lines)
            os.system('cls')
    elif user_input ==4: #Detele an existing customer file
        os.system('cls')
        files=os.listdir(user_dir)
        for file in files:
            print(file)
        file_name=input("Enter the file name which will be deleted: ")
        path_name=os.path.join(user_dir,file_name)
        if os.path.exists(path_name):
            os.remove(path_name)
        else:
            print("The file doesn't exist")
    elif user_input ==5:
        break
    else:
        print("Not valid value")
