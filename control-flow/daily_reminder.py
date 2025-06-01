# Prompt for task input
Task = input("Enter the task description: ")
Priority = input("Enter the task's priority (high, medium, low): ").lower()
Time_bound = input("Is the task time-bound? (yes or no): ").lower()

# Process the task based on Priority
match Priority:
    case "high":
        reminder = f"Reminder: '{Task}' is a HIGH priority task."
    case "medium":
        reminder = f"Reminder: '{Task}' is a MEDIUM priority task."
    case "low":
        reminder = f"Reminder: '{Task}' is a LOW priority task."
    case _:
        reminder = f"Reminder: '{Task}' has an unknown priority."

# Modify reminder if time-bound
if Time_bound == "yes":
    reminder += " It requires immediate attention today!"

# Print the customized reminder
print(reminder)
 