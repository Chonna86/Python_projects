result = 0
operand = None
operator = None
wait_for_number = True

while wait_for_number :
    enter_operand = input()
    try :
        result = int(enter_operand)
    except ValueError :
        print(f"{enter_operand} is not number. Try again ")
        continue
    wait_for_number = False
while operator != "=" :
    if wait_for_number == False :
        operator = input()
        if operator not in "+-*/=" :
            print(f"{operator} is not '+','-','*','/' or '='. Try again")
            continue
        wait_for_number = True
        if operator == '=' :
            break

    if wait_for_number :
        enter_operand = input()
        try :
            operand = int(enter_operand)
        except ValueError :
            print(f"{enter_operand} is not number. Try again ")
            continue
        wait_for_number = False
            
    if operator == '+' :
        result += operand
    elif operator == '-' :
        result -= operand
    elif operator == '*' :
        result *= operand
    elif operator == '/' :
        if operand == 0 :
            print("Error. Devision by zero is not allowed ")
            continue
        result /= operand

print(f"Result : {result}")
    