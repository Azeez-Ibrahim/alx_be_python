from datetime import datetime,timedelta


def display_current_datetime():
    """
    a function that displays the current date and time
    """
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {current_date}")


display_current_datetime()
num_days = int(input("Enter the number of days to add to the current date: "))


def calculate_future_date():
    """
    a function that calculates a future date
    """
    current_date = datetime.now()
    future_date = current_date + timedelta(days=num_days)
    print(f"Future date: {future_date.strftime("%Y-%m-%d")}")

calculate_future_date()
