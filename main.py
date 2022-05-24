def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return "Please enter the contact like this:\nName: number"
        except KeyError:
            return "This contact doesn't exist."
        except ValueError:
            return "Invalid command entered."

    return inner


def greeting():
    return "How can I help you?"


def to_exit():
    return "Good bye"


def to_exit1():
    return "Good bye"


def to_exit2():
    return "Good bye"


def to_exit3():
    return "Good bye"


data = {}


@input_error
def add_contact(*args):
    data.update({args[0]: args[1]})
    return f'Contact {args[0].title()} has added successfully'


@input_error
def change_number(*args):
    data[args[0]] = args[1]
    return f'Phone for contact {args[0].title()} has changed successfully'


@input_error
def del_number(*args):
    del data[args[0]]
    return f'Phone for contact {args[0].title()} has deleted successfully'


@input_error
def print_phone(*args):
    return data[args[0]]


def show_all():
    return "\n".join([f"{k.title()}: {v}" for k, v in data.items()]) if len(data) > 0 else 'Contacts are empty'


all_commands = {
    greeting: "hello",
    add_contact: "add",
    change_number: "change",
    print_phone: "phone",
    show_all: "show all",
    to_exit: "good bye",
    to_exit1: "close",
    to_exit2: "exit",
    to_exit3: ".",
    del_number: "del"
}


def command_parser(user_input_lower):
    commands_value = ""
    command = ""
    for key, value in all_commands.items():
        if user_input_lower.startswith(value):
            command = key
            commands_value = user_input_lower.replace(value, "").split()
        else:
            continue
    return command, commands_value


def main():
    while True:
        user_input = input(">>> ").title()
        user_input_lower = user_input.lower()
        command, parser_data = command_parser(user_input_lower)
        print(command(*parser_data))
        if command == to_exit or command == to_exit1 or command == to_exit2 or command == to_exit3:
            break


if __name__ == "__main__":
    main()
