Weekly Task & Habit Tracker

This project is a Python-based CLI tool that allows you to track tasks and habits across the week. It lets you:

    i. Add, remove, and mark tasks and habits as complete
    ii. View daily and weekly progress
    iii. Maintain organized records of your productivity

##Features

    #Add Tasks/Habits: Enter daily tasks or habits you want to track.
    #Mark Complete: Check off your accomplishments.
    #Remove Items: Delete outdated or irrelevant tasks/habits.
    #Progress Reports: Get a quick view of daily or weekly activity.

#Usage
How to Use the Weekly Task & Habit Tracker

1. Launch the Application
Make sure you have installed Python 3.9 or later.

#Run the script:    
##To run in interactive mode: python habit_task_tracker.py

##To run in HPC batch mode:
##Edit the script (habit_task_tracker.py) to comment out the main_menu() call and run via:
sbatch submit_habit_task.sh

2. Navigate the Main Menu
Once started, you’ll see options like:

=== Weekly Task & Habit Tracker ===
1. Add Task or Habit
2. Mark Task or Habit as Complete
3. Remove Task or Habit
4. View Report (Weekly or Daily)
5. Exit
   
Choose an option by typing its number and pressing Enter.
3. Add Tasks
- Choose Option 1.
- Enter “Task” when asked.
- Enter the day of the week (e.g., Monday).
- Enter the name of your task.

The task will be added and marked as incomplete by default.
4. Add Habits
- Choose Option 1.
- Enter “Habit” when asked.
- Enter the name of your habit.
- The habit will be added for all 7 days (initially marked as incomplete).

5. Mark as Complete
- Choose Option 2.
- Enter “Task” or “Habit”.
- Enter the required details (day/task name or habit name).
- The status will be updated to Completed.

6. Remove Items
- Choose Option 3.
- Enter “Task” or “Habit”.
- Enter the required details.
- The item will be removed from the tracker.

7. View Reports
- Choose Option 4.
- Enter “Weekly” for a summary across all days.
- Enter “Daily” and a specific day for a breakdown of tasks and habits.

8. Exit
- Choose Option 5 to save your progress and end the program.

#Additional Tips
- All inputs (day, task names, habit names) are case‑insensitive.
- If an invalid option is entered, the program will prompt you to try again.
- Use this tool every day to build consistency and track your productivity!

##Notes
#Compatible with Python 3.9 and higher.
#Supports both interactive and batch/HPC execution.
#Output saved to habit_task_output.txt and habit_task_error.txt when run via HPC.

