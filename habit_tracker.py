#!/bin/py

# This codes will create a list containing all the days of the week 

# List of all days of the week
days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Dictionary to track habits for the week
habits = {}

# Dictionary to store tasks, with each day as a key and an empty dictionary as value
tasks = {day: {} for day in days_of_week}



#Add Tasks----------------------

def add_task():
    # Ask for the day
    day = input("Enter the day you want to add the task to: ").strip().title()

    # Validate the day
    if day not in days_of_week:
        print("Invalid day. Please enter a valid day (e.g., Monday).")
        return

    # Ask for the task name
    task_name = input("Enter the task name: ").strip()

    # Check if the task already exists
    if task_name in tasks[day]:
        print(f"The task '{task_name}' already exists on {day}.")
    else:
        # Store the task and set as not completed
        tasks[day][task_name] = False
        print(f"Task '{task_name}' added to {day}.")

#Add Habits---------------------

def add_habit():
    # Ask for the habit name
    habit_name = input("Enter the name of the habit (e.g., 'Drink Water'): ").strip().title()

    # Check if the habit already exists
    if habit_name in habits:
        print(f"Habit '{habit_name}' already exists.")
        return

    # Create a nested dictionary with all 7 days set to False
    habits[habit_name] = {day: False for day in days_of_week}
    print(f"Habit '{habit_name}' has been added for all days of the week.")

# Marking Tasks and Habits as Complete

my_dict = {
    "a": 1,
    "b": 2,
    "c": 3
}

# Loop through keys and values
for habit, days in habits.items():
    print(f"\nHabit: {habit}")
    for day, completed in days.items():
        status = "Great Job" if completed else "Put more effort"
        print(f"  {day}: {status}")



#loop through keys----------------------------------------------

import datetime

def mark_task_complete():
    uncompleted_tasks = []

    # Display all uncompleted tasks
    for day, day_tasks in tasks.items():
        for task, completed in day_tasks.items():
            if not completed:
                uncompleted_tasks.append((day, task))

    if not uncompleted_tasks:
        print("All tasks are already completed!")
        return

    print("\nUncompleted Tasks:")
    for day, task in uncompleted_tasks:
        print(f"- {task} (Day: {day})")

    # Ask user for day and task name
    day = input("\nEnter the day the task belongs to: ").strip().title()
    if day not in days_of_week:
        print("Invalid day. Please enter a valid weekday.")
        return

    task_name = input("Enter the task you completed: ").strip()
    if task_name not in tasks[day]:
        print(f"Task '{task_name}' not found on {day}.")
        return


# Mark task as complete-----------------------------------------------------

tasks[day][task_name] = True
    print(f"Task '{task_name}' on {day} marked as complete.")

    # BONUS: Check if the task is from an earlier day
    today_index = datetime.datetime.today().weekday()
    task_day_index = days_of_week.index(day)
    if task_day_index < today_index:
        print("Task marked as complete. Better late than never!")

#Mark habit as complete

def mark_habit_complete():
    day = input("Enter the day you completed the habit: ").strip().title()
    if day not in days_of_week:
        print("Invalid day. Please enter a valid weekday.")
        return

    habit_name = input("Enter the name of the habit: ").strip().title()
    if habit_name not in habits:
        print(f"Habit '{habit_name}' not found.")
        return

    # Mark habit as completed for the day
    habits[habit_name][day] = True
    print(f"✅ Habit '{habit_name}' marked as complete for {day}.")

#Part 4: Removing Tasks and Habits_____________________

#Function to Remove a Task

def remove_task():
    day = input("Enter the day of the task you want to remove: ").strip().title()
    if day not in days_of_week:
        print("Invalid day entered.")
        return

    if not tasks[day]:
        print(f"There are no tasks for {day}.")
        return

    # List tasks for the day
    print(f"Tasks for {day}:")
    for task_name in tasks[day]:
        print(f" - {task_name}")

    task_name = input("Enter the name of the task you want to remove: ").strip()
    if task_name in tasks[day]:
        del tasks[day][task_name]
        print(f"✅ Task '{task_name}' has been removed from {day}.")
    else:
        print(f"Task '{task_name}' does not exist on {day}.")


# Function to Remove a Habit

def remove_habit():
    if not habits:
        print("There are no habits being tracked.")
        return

    # List habits
    print("\nCurrent habits being tracked:")
    for habit_name in habits:
        print(f" - {habit_name}")

    habit_name = input("\nEnter the name of the habit you want to remove: ").strip().title()
    if habit_name in habits:
        del habits[habit_name]
        print(f"✅ Habit '{habit_name}' has been removed.")
    else:
        print(f"Habit '{habit_name}' does not exist.")

#Generating Weekly and Daily Reports--------------------------

#Weekly Report

def weekly_report():
    print("\n=== Weekly Report ===\n")

    # Habits
    if habits:
        print("Habit Completion Summary (out of 7):")
        for habit_name, days in habits.items():
            completed_count = sum(1 for status in days.values() if status)
            print(f" - {habit_name}: {completed_count}/7 days ✅")
    else:
        print("No habits found.")

    # Tasks
    all_tasks = []
    completed_tasks = []
    for day, day_tasks in tasks.items():
        for task_name, status in day_tasks.items():
            if status:
                completed_tasks.append(f"{task_name} ({day})")
            all_tasks.append((task_name, day))

    if all_tasks:
        not_completed_tasks = [
            f"{name} ({day})" for (name, day) in all_tasks if f"{name} ({day})" not in completed_tasks
        ]
        print("\nCompleted Tasks ✅:", ", ".join(completed_tasks) if completed_tasks else "None")
        print("Not Completed Tasks ❌:", ", ".join(not_completed_tasks) if not_completed_tasks else "None")
    else:
        print("\nNo tasks found.")



#Daily Report

def daily_report():
    day = input("\nEnter the day for the daily report (e.g., Monday): ").strip().title()
    if day not in days_of_week:
        print("Invalid day entered.")
        return

    print(f"\n=== {day} Report ===\n")

    # Tasks
    if tasks[day]:
        print("Tasks for the Day:")
        for task_name, status in tasks[day].items():
            mark = "✅" if status else "❌"
            print(f" - {task_name}: {mark}")
    else:
        print("No tasks found for this day.")

    # Habits
    if habits:
        print("\nHabits for the Day:")
        for habit_name, days in habits.items():
            mark = "✅" if days.get(day, False) else "❌"
            print(f" - {habit_name}: {mark}")
    else:
        print("\nNo habits found.")



#Part 6:Building the Main Menu System--------------------------------------

#Main Menu System

def main_menu():
    while True:
        print("\n=== Weekly Task & Habit Tracker ===")
        print("1. Add Task or Habit")
        print("2. Mark Task or Habit as Complete")
        print("3. Remove Task or Habit")
        print("4. View Report (Weekly or Daily)")  
        print("5. Exit")  

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            add_choice = input("Add a (T)ask or (H)abit? ").strip().lower()
            if add_choice == "t":
                add_task()
            elif add_choice == "h":
                add_habit()
            else:
                print("Invalid choice. Please enter 'T' or 'H'.")

        elif choice == "2":
            mark_choice = input("Mark a (T)ask or (H)abit as Complete? ").strip().lower()
            if mark_choice == "t":
                mark_task_complete()
            elif mark_choice == "h":
                mark_habit_complete()
            else:
                print("Invalid choice. Please enter 'T' or 'H'.")

        elif choice == "3":
            remove_choice = input("Remove a (T)ask or (H)abit? ").strip().lower()
            if remove_choice == "t":
                remove_task()
            elif remove_choice == "h":
                remove_habit()
            else:
                print("Invalid choice. Please enter 'T' or 'H'.")

        elif choice == "4":
            report_choice = input("View (W)eekly or (D)aily Report? ").strip().lower()
            if report_choice == "w":
                weekly_report()
            elif report_choice == "d":
                daily_report()
            else:
                print("Invalid choice. Please enter 'W' or 'D'.")

        elif choice == "5":
            print("\nThank you for using the Weekly Task & Habit Tracker! 👋")
            break

        else:
            print("\nInvalid choice. Please select a number between 1 and 5.")

# Run the Main Menu
main_menu()










