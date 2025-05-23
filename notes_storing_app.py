import argparse
import datetime

# This creates a calendar with notes
# The user can add, remove notes or list all notes
# From a terminal run "python manages_notes_application.py <txt filename where the notes will be stores"

def append_note(note,file_path):
    with open(file_path, 'a') as file:
        x = datetime.datetime.now()
        file.write(x.strftime("Date:%Y-%b-%d Time: %H:%M:%S")+ "  NOTE  "+ note +'\n')

def list_all_notes(file_path):
    with open(file_path, 'r') as file:
        for i,line in enumerate(file.readlines()):
            print(f"{i+1}) {line}", end="")

def delete_notes(line_number,file_path):
    with open(file_path, 'r+') as file:
        lines =file.readlines()
        if line_number > len(lines) or line_number == 0 :
            print("Invalid line number,please try again")
        else:
            lines.pop(line_number-1)
            file.seek(0)
            file.truncate()
            file.writelines(lines)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = "A command-line note-taken application")
    parser.add_argument('path', help = 'Enter the note path')
    args = parser.parse_args()

  
    while True:
        print("  What would you like to do?\n")
        user_input = input ("(1) Add a new note, (2) Delete a note, (3) List all notes, (4) EXIT: ")
        if user_input == '1':
            note= input("Enter a new note: ")
            append_note (note, args.path)
        elif user_input == '2':
            list_all_notes(args.path)
            try:
                line_number= int(input("Enter the delete line number: "))
                delete_notes(line_number, args.path)
            except ValueError:
                print("Not accepted value, enter an int value")

        elif user_input == '3':
            list_all_notes(args.path)
        elif user_input == '4':   
            break
        else:
            print("Incorrect value")   
            



