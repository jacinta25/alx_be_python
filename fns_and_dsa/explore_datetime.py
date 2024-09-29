from datetime import datetime, timedelta

# Part 1: Display the current date and time
def display_current_datetime():
    current_date = datetime.now()  # Get the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # Format it to "YYYY-MM-DD HH:MM:SS"
    print(f"Current Date and Time: {formatted_date}")

# Part 2: Calculate a future date
def calculate_future_date():
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))  # Updated prompt message
        future_date = datetime.now() + timedelta(days=days_to_add)  # Calculate future date
        formatted_future_date = future_date.strftime("%Y-%m-%d")  # Format it to "YYYY-MM-DD"
        print(f"Future Date after {days_to_add} days: {formatted_future_date}")
    except ValueError:
        print("Please enter a valid integer for the number of days.")

# Main function to run both parts
def main():
    display_current_datetime()  # Display current date and time
    calculate_future_date()  # Calculate and display future date

if __name__ == "__main__":
    main()

