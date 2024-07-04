def perform_operation(num1, num2, operation):
    """
    a function that performs basic arithmetic operations
    """
    if operation == "add":
        return num1 + num2
    if operation == "subtract":
        return num1 - num2
    if operation == "multiply":
        return num1 * num2
    if  num2 == 0:
        return "ZeroDivisionError"
    elif operation == "divide":
        return num1 / num2
