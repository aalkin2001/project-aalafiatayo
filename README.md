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
##To run in interactive mode: python habit_task_tracker.py

##To run in HPC batch mode:
##Edit the script (habit_task_tracker.py) to comment out the main_menu() call and run via:
sbatch submit_habit_task.sh

##Directory Structure

=== Weekly Task & Habit Tracker ===
1. Add Task or Habit
2. Mark Task or Habit as Complete
3. Remove Task or Habit
4. View Report (Weekly or Daily)
5. Exit


##Notes
#Compatible with Python 3.9 and higher.
#Supports both interactive and batch/HPC execution.
#Output saved to habit_task_output.txt and habit_task_error.txt when run via HPC.

