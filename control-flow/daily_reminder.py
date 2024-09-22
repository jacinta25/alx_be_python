# Prompt for a single task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Generate the reminder based on priority and time sensitivity
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
        if time_bound == "yes":
            reminder += " that requires immediate attention today!"
        else:
            reminder += "."
    case "medium":
        reminder = f"'{task}' is a medium priority task"
        if time_bound == "yes":
            reminder += " that should be addressed soon."
        else:
            reminder += " Consider doing it when you have time."
    case "low":
        reminder = f"'{task}' is a low priority task."
        if time_bound == "yes":
            reminder += " Try to complete it soon."
        else:
            reminder += " Consider completing it when you have free time."
    case _:
        reminder = "Invalid priority level."

# Print the reminder
print(reminder)
