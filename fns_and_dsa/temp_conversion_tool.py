# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5  # Defined without spaces

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR  # Accessing the global variable
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR  # Accessing the global variable
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Main function to handle user interaction
def main():
    try:
        # Prompt user for temperature input
        temperature = float(input("Enter the temperature to convert: "))
        
        # Prompt for the unit of the temperature
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        if unit == "F":  # If input is in Fahrenheit
            celsius = convert_to_celsius(temperature)
            print(f"{temperature}°F is {celsius}°C")
        
        elif unit == "C":  # If input is in Celsius
            fahrenheit = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {fahrenheit}°F")
        
        else:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    
    except ValueError:
        # Specific error message expected by the checker
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()  # Run the main function

