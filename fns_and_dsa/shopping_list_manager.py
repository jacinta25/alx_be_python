def display_menu():
    print("Shopping List Manager")  # Ensure exact phrase is printed
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # Start with an empty list
    
    while True:
        display_menu()  # Display the menu
        
        choice = input("Enter your choice: ").strip()  # Get user input and remove any extra spaces
        
        if choice == '1':  # Add an item
            item = input("Enter the item to add: ").strip()
            shopping_list.append(item)  # Add the item to the list
            print(f"'{item}' has been added to the list.")
        
        elif choice == '2':  # Remove an item
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:  # Check if the item exists in the list
                shopping_list.remove(item)  # Remove the item
                print(f"'{item}' has been removed from the list.")
            else:
                print(f"'{item}' not found in the shopping list.")
        
        elif choice == '3':  # View the list
            if shopping_list:  # If the list is not empty
                print("\nYour Shopping List:")
                for index, item in enumerate(shopping_list, 1):
                    print(f"{index}. {item}")  # Print each item with its index
            else:
                print("Your shopping list is empty.")
        
        elif choice == '4':  # Exit
            print("Goodbye!")
            break  # Exit the loop and the program
        
        else:
            print("Invalid choice. Please try again.")  # Handle invalid choices

if __name__ == "__main__":
    main()  # Start the program
