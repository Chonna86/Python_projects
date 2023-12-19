from search import search_quotes

if __name__ == "__main__":
    while True:
        user_input = input("Enter command: ")
        result = search_quotes(user_input)
        print(result)