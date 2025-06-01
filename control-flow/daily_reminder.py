# Prompt for task input
task = input("Enter the task description: ")
priority = input("Enter the task's priority (high, medium, low): ").lower()
time_bound = input("Is the task time-bound? (yes or no): ").lower()

# Process the task based on priority
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a HIGH priority task."
    case "medium":
        reminder = f"Reminder: '{task}' is a MEDIUM priority task."
    case "low":
        reminder = f"Reminder: '{task}' is a LOW priority task."
    case _:
        reminder = f"Reminder: '{task}' has an unknown priority."

# Modify reminder if time-bound
if time_bound == "yes":
    reminder += " It requires immediate attention today!"

# Print the customized reminder
print(reminder)
