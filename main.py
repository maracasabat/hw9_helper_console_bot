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


def greeting(*args):
    return "How can I help you?"


def to_exit(*args):
    return "Good bye"


data = {}


@input_error
def add_contact(*args):
    data.update({str(args[0]): int(args[1])})
    return f'Contact {args[0].title()} has added successfully'


@input_error
def change_number(*args):
    data[args[0]] = int(args[1])
    return f'Phone for contact {args[0].title()} has changed successfully'


@input_error
def del_number(*args):
    del data[args[0]]
    return f'Phone for contact {args[0].title()} has deleted successfully'


@input_error
def print_phone(*args):
    return data[args[0]]


def show_all(*args):
    return "\n".join([f"{k.title()}: {v}" for k, v in data.items()]) if len(data) > 0 else 'Contacts are empty'


all_commands = {
    greeting: ["hello", "hi"],
    add_contact: ["add", "new"],
    change_number: ["change", ],
    print_phone: ["phone", "number"],
    show_all: ["show all", "show"],
    to_exit: ["good bye", "close", "exit", ".", "bye"],
    del_number: ["del", "delete"]
}


def command_parser(user_input: str):
    for key, value in all_commands.items():
        for i in value:
            if user_input.lower().startswith(i.lower()):
                return key, user_input[len(i):].strip().split()


def main():
    while True:
        user_input = input(">>> ")
        command, parser_data = command_parser(user_input)
        print(command(*parser_data))
        if command is to_exit:
            break


if __name__ == "__main__":
    main()
