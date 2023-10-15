class Human:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Меня зовут {self.name} и мне {self.age} лет.")   
person = Human('Rebecca',35)
person_1 = Human('Bob',45)
person.introduce()
print(person.name)
print(person.age)
print(person_1.name)
while True:
    user_input = input()
    print(user_input)
    if user_input == "exit":
        break