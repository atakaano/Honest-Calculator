msg_ = ["Enter an equation", "Do you even know what numbers are? Stay focused!",
        "Yes ... an interesting math operation. You've slept through all classes, haven't you?", "Yeah... division by zero. Smart move...",
        "Do you want to store the result? (y / n):", "Do you want to continue calculations? (y / n):",
        " ... lazy", " ... very lazy", " ... very, very lazy", "You are", "Are you sure? It is only one digit! (y / n)",
        "Don't be silly! It's just one number! Add to the memory? (y / n)", "Last chance! Do you really want to embarrass yourself? (y / n)"]

valid_operations = ["+", "-", "*", "/"]
running = True
memory = 0


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mult(a, b):
    return a * b


def div(a, b):
    return a / b if b != 0.00 else print(msg_[3])

def is_one_digit(a):
    try:
        if a == int(a):
            return -10 < a < 10
    except ValueError:
        return False

def calc(a, op, b):
    if op == "+":
        res = add(a, b)
    elif op == "-":
        res = sub(a, b)
    elif op == "*":
        res = mult(a, b)
    elif op == "/":
        res = div(a, b)
    return res

def check(a, op, b):
    msg = ""
    if is_one_digit(a) and is_one_digit(b):
        msg += msg_[6]
    if (a == 1 or b == 1) and op == "*":
        msg += msg_[7]
    if (a == 0 or b == 0) and (op == "*" or op == "+" or op == "-"):
        msg += msg_[8]
    if msg:
        msg = msg_[9] + msg
        print(msg)



while running:
    x, oper, y = input(msg_[0]).split()
    try:
        if x == "M":
            x = memory
        if y == "M":
            y = memory
        x, y = float(x), float(y)
    except ValueError:
        print(msg_[1])
        continue

    if oper not in valid_operations:
        print(msg_[2])
        continue

    check(x, oper, y)

    result = calc(x, oper, y)
    if result is not None:
        print(result)
    else:
        continue

    answer = ""
    while answer != "y" and answer != "n":
        print(msg_[4])
        answer = input()
        if answer == "y":
            if is_one_digit(result):
                msg_index = 10
                while msg_index <= 12:
                    print(msg_[msg_index])
                    answer = input()
                    if answer == "y":
                        msg_index += 1
                    else:
                        break
                else:
                    memory = result
            else:
                memory = result

    answer = ""
    while answer != "y" and answer != "n":
        print(msg_[5])
        answer = input()
        if answer == "n":
            running = False
