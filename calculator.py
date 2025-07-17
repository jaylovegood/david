class InvalidFormatException(Exception):
    pass

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a / b

def parse(exp):
    
    try:
        a, op, b = tuple(exp.split())
        a = int(float(a))
        b = int(float(b))
    except:
        raise InvalidFormatException
    
    return a, b, op

def main():
    # a = int(float(input()))
    # b = int(float(input()))

    # op = input()

    exp = input("Enter expression: ")

    try:
        a, b, op = parse(exp)
    except InvalidFormatException:
        print("Invalid input expression format.")
        return
    
    if op == '+':
        result = add(a, b)

    elif op == '-':
        result = subtract(a, b)

    elif op == '*':
        result = multiply(a, b)

    elif op == '/':
        try: 
            result = divide(a, b)
        except:
            print("Error: Division by zero.")
            return
        
    else:
        print("Invalid operator.")
        return
    
    print(f"Result: {result}")

if __name__=="__main__":
    main()