

contacts = {}


# First, let's create a decorator function to handle errors
def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Invalid command format"
    return wrapper

# Now we call the decorator function for each of the following functions on user input.
# Next let's create a function for entering user input into our dictionary(contacts = {})
@input_error
def add_contact(command):
    _, name, phone = command.split()
    contacts[name] = phone
    return f"Contact {name} added with phone number {phone}"


'''Now let's create a function to enter the data entered by the user into our dictionary, 
if the user has changed the phone number of an existing contact in the dictionary''' 
@input_error
def change_phone(command):
    _, name, new_phone = command.split()
    contacts[name] = new_phone
    return f"Phone number for {name} updated to {new_phone}"


# Now let's create a function to display the phone number of the contact whose name the user entered
@input_error
def get_phone(command):
    _, name = command.split()
    phone = contacts.get(name, "Contact not found")
    return f"Phone number for {name}: {phone}"

# Now let's create a function to output all the data entered by the user
@input_error
def show_all_contacts(command):
    if not contacts:
        return "No contacts found"
    contact_list = "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    return contact_list


'''Now let's create the main function, which will do all the interaction 
with the user and will perform all the logic of the program'''
def main():
    print("How can I help you?")
    while True:
        user_input = input().strip().lower()

        if user_input in ("good bye", "close", "exit"):
            print("Good bye!")
            break
        elif user_input == "hello":
            print("How can I help you?")
        elif user_input.startswith("add"):
            result = add_contact(user_input)
            print(result)
        elif user_input.startswith("change"):
            result = change_phone(user_input)
            print(result)
        elif user_input.startswith("phone"):
            result = get_phone(user_input)
            print(result)
        elif user_input == "show all":
            result = show_all_contacts(user_input)
            print(result)
        else:
            print("Invalid command")

if __name__ == "__main__":
    main()