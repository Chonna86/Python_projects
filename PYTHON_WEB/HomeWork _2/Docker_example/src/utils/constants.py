from colorama import Fore

B = Fore.YELLOW
G = Fore.GREEN
Y = Fore.BLUE
R = Fore.RESET

WARNING_MESSAGE = (
    "WARNING! This operation may be risky!\nAre you sure that you want to sort files in this "
    "directory? (Y/N)\n"
)
ABORTING_OPERATION_MESSAGE = "Aborting operation..."

SORTING_PROGRESS_MESSAGE = rf"Sorting files in "

INVITE_MESSAGE = (
    f"\n Enter your command if you know what to do \n"
    f"or type 'help' for the list of available commands\n"
    f" >>> "
)

TYPE_OR_ATTRIBUTE_ERROR_MESSAGE = (
    "\nInvalid command, please choose one from the following list:\n "
)

UNDEFINED_ERROR_MESSAGE = "Something wrong have happened: "

GREETING_MESSAGE = "How can I help you?"

BYE_MESSAGE = "Good bye!"

# functional commands have only two words (according to current parser logic)
BOT_COMMANDS = [
    "hi",
    "hello",
    "close",
    "exit",
    "good bye",
    "add contact",
    "find contact",
    "delete contact",
    "add note",
    "find note",
    "edit note_text",
    "add tags",
    "delete note",
    "sort dir",
    "help",
    "change birthday",
    "search contacts",
    "show all",
    "add phone",
    "list notes",
]

HELP_INFO = f"""
    {B}add contact{R} [ firstname ] [ lastname ] or {B}add contact{R} [ firstname ]  - {Y}adds the contact with corresponding name (and lastname) to the address book
    {B}add note{R} [ text ] - {Y}adds a note with the corresponding text
    {B}add phone{R} [ name ] [ phone ] - {Y}adds the contact with name and phone to the address book, the phone number must be 8 or 10 digits long
    {B}add tags{R} [ text ] [ #tag ] - {Y}adds one or more tags to the note with corresponding text
    {B}change birthday{R} - [name] [new birthday in format xx/xx/xxxx] - {Y}changes the birthday of the contact with corresponding name
    {B}close{R} / {B}exit{R} / {B}good bye{R} - {Y}exits the program
    {B}delete contact{R} [ name ] - {Y}deletes the contact with corresponding name from the address book
    {B}delete note{R} [ text / #tag ] - {Y}deletes the note with corresponding text or tag
    {B}edit note_text{R} [ text ] [ new text ] - {Y}edits the note with corresponding text
    {B}find contact{R} [ name ] or {B}find contact{R} [first name] [second name] - {Y}searches for a contact by name or by first and last name
    {B}find note{R} [ text / #tag ] - {Y}searches for a note by text or tag
    {B}hello{R} / {B}hi{R} - {Y}greets the user
    {B}help{R} - {Y}shows the list of available commands
    {B}list notes{R} - {Y}shows all notes 
    {B}search contacts{R} [ ... ] - {Y}searches for a contact by partial name or number
    {B}show all{R} - {Y}shows all contacts
    {B}sort dir{R} [ path to dir ] - {Y}sorts files in the directory{R}
"""
