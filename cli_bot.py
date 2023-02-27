import re

contacts = {}  # Empty dictionary to store contacts

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
            return "Please enter name and correct phone number separated by a space"

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

@input_error
def hello(*_):
    return "How can I help you?"

# fnc to add a new contact to the phonebook
@input_error
def add_contact(*args, **kwargs):
    name = args[0]
    phone = normal_phone(args[1])
    if phone:
        contacts[name] = phone
        return f"{name} has been added to the phonebook"
    else:
        return ""


# fnc to change the phone number of an existing contact
@input_error
def change_contact(*args, **kwargs):
    name = args[0]
    phone = normal_phone(args[1])
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
    hello: 'hello',
    show_all: "show all",
    add_contact: "add",
    change_contact: "change",
    find_phone: "phone",
}

# fnc to keep only needed part of the command
def remove_unnecessary_text(text):
    regex_pattern = "|".join(map(re.escape, COMMANDS.values()))
    match = re.search(regex_pattern, text.lower())
    if not match:
        return text
    start_index = match.start()
    return text[start_index:]


def command_handler(user_input: str):
    for command, command_words in COMMANDS.items():
        if user_input.lower().startswith(command_words):
            return command, user_input[len(command_words):].strip().split(" ")
    return None, None


def main():
    while True:
        user_input = input("Enter a command: ")
        cmd = remove_unnecessary_text(user_input)
        command, data = command_handler(cmd)
        if command:
            print(command(*data))
        elif any(word in user_input.lower() for word in ['exit', 'close', 'good bye', 'goodbye']):
            print('Good bye!')
            break
        else:
            print('Command is not supported. Try again.')


if __name__ == "__main__":
    main()