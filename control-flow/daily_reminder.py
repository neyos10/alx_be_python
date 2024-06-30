# daily_reminder.py


task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")


match priority:
    case "high":
        if time_bound.lower() == "yes":
            reminder = f"'{task}' is a high priority task that requires immediate attention today!"
        else:
            reminder = f"Note: '{task}' is a high priority task. Try to complete it as soon as possible."
    case "medium":
        if time_bound.lower() == "yes":
            reminder = f"'{task}' is a medium priority task that needs to be done today!"
        else:
            reminder = f"Note: '{task}' is a medium priority task. You should consider doing it soon."
    case "low":
        if time_bound.lower() == "yes":
            reminder = f"'{task}' is a low priority task, but it needs to be done today!"
        else:
            reminder = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."

print("Reminder:", reminder)