def perform_operation(num1=None, num2=None, operation=None):
    """
    a function that performs basic arithmetic operations
    """
    if operation == "add":
        return num1 + num2
    if operation == "subtract":
        return num1 - num2
    if operation == "multiply":
        return num1 * num2
    if operation == "divide" and num2 != 0:
        return num1 / num2
    else:
        return "ZeroDivisionError"