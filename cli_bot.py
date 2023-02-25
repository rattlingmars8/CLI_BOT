contacts = {} # Empty dictionary to store contacts

# Decorator function for common input errors
def input_error(func):
    def wrapper(*args):
        try:
            return func(*args) # Call the decorated function with the given arguments
        except KeyError:
            return "This contact doesn't exist in the phonebook"
        except ValueError:
            return "Please enter name and correct phone number separated by a space"
        except IndexError:
            return "Please enter a contact name"
    return wrapper

# ADDITIONAL!!! Function to normalize phone numbers
def normal_phone(phone):
    checked_phone = ''
    for ch in phone:
        if ch.isdigit():
            checked_phone += ch
    if len(checked_phone) == 10:
        new_phone = '+38' + checked_phone
        return new_phone
    elif len(checked_phone) == 12 and checked_phone.startswith('38'):
        new_phone = '+' + checked_phone
        return new_phone
    elif len(checked_phone) == 11:
        print("Phone is not correct")
    elif len(checked_phone) < 10:
        print("Phone is not correct")
    else:
        new_phone = checked_phone
        return new_phone

# fnc to add a new contact to the phonebook
@input_error
def add_contact(name, phone):
    if phone:
        contacts[name] = phone
        return f"{name} has been added to the phonebook"
    else:
        return ""

# fnc to change the phone number of an existing contact
@input_error
def change_contact(name, phone):
    if phone:
        contacts[name] = phone
        return f"The phone number for {name} has been updated"
    else:
        return ""

# fnc to find the phone number of a given contact
@input_error
def find_phone(name):
    return f"The phone number for {name} is {contacts[name]}"

# fnc to show all contacts and their phone numbers
@input_error
def show_all():
    output = ""
    for name, phone in contacts.items():
        output += f"{name}: {phone}\n"
    return output



def main():
    while True:
        command = input("Enter a command: ").split()
        lower_command = [command.lower() for command in command]
        if not command:
            continue
        elif 'hello' in lower_command:
            print("How can I help you?")
        elif 'add' in lower_command:
            add_index = lower_command.index('add')
            if len(command) < add_index + 3: # in case user forgot to provide a name or phone number
                print("Please enter a contact name and phone number") 
            else:
                print(add_contact(command[add_index+1], normal_phone(command[add_index+2]))) # call the add_contact with the following commands indexes(name -> phone)
        elif 'change' in lower_command:
            change_index = lower_command.index('change')
            if len(command) < change_index + 3: # in case user forgot to provide a name or phone number
                print("Please enter a contact name and phone number")
            else:
                print(change_contact(command[change_index+1], normal_phone(command[change_index+2]))) # call the change_contact with the following commands indexes(name -> phone)
        elif 'phone' in lower_command:
            phone_index = lower_command.index('phone')
            if len(command) < phone_index + 2:
                print("Please enter a contact name")
            else: 
                print(find_phone(command[phone_index+1]))
        # check if the user input command contains the word 'show' and then the word 'all' 
        elif 'show' in lower_command and lower_command.index("show") < len(lower_command) - 1 and lower_command[lower_command.index("show") + 1] == "all": 
            print(show_all())
        # exit commands with the same logic as previous elif statement
        elif 'exit' in lower_command or 'close' in lower_command or ('good' in lower_command and lower_command.index("good") < len(lower_command) - 1 and lower_command[lower_command.index("good") + 1] == "bye"):
            print('Good bye!')
            break

if __name__ == "__main__":
    main()
