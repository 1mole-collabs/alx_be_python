# Prompt user for task details
task = input("Enter the task description: ")
priority = input("Enter the task's priority (high, medium, low): ").strip().lower()
time_bound = input("Is the task time-bound? (yes or no): ").strip().lower()

# Initialize the base reminder
reminder = f"Reminder: '{task}' is a"

# Process based on priority
match priority:
    case "high":
        reminder += " HIGH priority task."
    case "medium":
        reminder += " MEDIUM priority task."
    case "low":
        reminder += " LOW priority task."
    case _:
        reminder += " task with an UNKNOWN priority."

# Add time sensitivity message if applicable
if time_bound == "yes":
    reminder += " It requires immediate attention today!"

# Display the final reminder
print(reminder)
