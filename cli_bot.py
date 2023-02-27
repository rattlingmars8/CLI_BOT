import re

contacts = {}  # Empty dictionary to store contacts

# Function dict by it's command
# COMMANDS = {
#     'hello': lambda _: "How can I help you?",
#     'add': lambda args: add_contact(args[0], normal_phone(args[1])),
#     'change': lambda args: change_contact(args[0], normal_phone(args[1])),
#     'phone': lambda args: find_phone(args[0]),
#     'show all': lambda _: show_all(),
# }

# Decorator function for common input errors
def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(
                *args, **kwargs
            )  # Call the decorated function with the given arguments
        except KeyError:
            return "This contact doesn't exist in the phonebook"
        except ValueError:
            return "Please enter name and correct phone number separated by a space"
        except IndexError:
            return "Please enter a contact name"

    return wrapper


# ADDITIONAL!!! Function to normalize phone numbers
def normal_phone(phone):
    checked_phone = ""
    for ch in phone:
        if ch.isdigit():
            checked_phone += ch
    if len(checked_phone) == 10:
        new_phone = "+38" + checked_phone
        return new_phone
    elif len(checked_phone) == 12 and checked_phone.startswith("38"):
        new_phone = "+" + checked_phone
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
def add_contact(*args, **kwargs):
    name = args[0]
    phone = args[1]
    if phone:
        contacts[name] = phone
        return f"{name} has been added to the phonebook"
    else:
        return ""


# fnc to change the phone number of an existing contact
@input_error
def change_contact(*args, **kwargs):
    name = args[0]
    phone = args[1]
    if phone:
        contacts[name] = phone
        return f"The phone number for {name} has been updated"
    else:
        return ""


# fnc to find the phone number of a given contact
@input_error
def find_phone(*args, **kwargs):
    name = args[0]
    return f"The phone number for {name} is {contacts[name]}"


# fnc to show all contacts and their phone numbers
@input_error
def show_all(*args, **kwargs):
    output = ""
    for name, phone in contacts.items():
        output += f"{name}: {phone}\n"
    return output


COMMANDS = {
    show_all: ["show all", "show", "показати всі"],
    add_contact: ["add", "+", "додати"],
    change_contact: ["change", "змінити"],
    find_phone: ["find phone"],
}


# fnc to keep only needed part of the command
def remove_unnecessary_text(text):
    regex_pattern = "|".join(map(re.escape, COMMANDS.keys()))
    match = re.search(regex_pattern, text.lower())
    if not match:
        return text
    start_index = match.start()
    return text[start_index:]


def command_handler(user_input: str):
    for command, command_words in COMMANDS.items():
        for word in command_words:
            if user_input.startswith(word):
                return command, user_input.removeprefix(word).strip().split(" ")
    return None, None


def main():
    while True:
        user_input = input("Enter a command: ")
        command, data = command_handler(user_input)
        if command:
            print(command(*data))
        # only_useful_command = remove_unnecessary_text(command).split()
        # lower_command = [cmd.lower() for cmd in only_useful_command]
        # print(only_useful_command)
        # if not command:
        #     continue
        # # call the corresponding function with the remaining elements of the command
        # if only_useful_command[0].lower() in COMMANDS:
        #     try:
        #         result = COMMANDS[only_useful_command[0].lower()](only_useful_command[1:])
        #         print(result)
        #     except IndexError:
        #         print("Please enter name and correct phone number separated by a space")
        # elif only_useful_command[0].lower() == 'show' and only_useful_command[1].lower() == 'all':
        #     result = COMMANDS['show all'](only_useful_command[1:])
        #     print(result)
        # elif any(word in lower_command for word in ['exit', 'close', 'good bye', 'goodbye']):
        #     print('Good bye!')
        #     break
        # else:
        #     print('Command is not supported. Try again.')


if __name__ == "__main__":
    main()
