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













