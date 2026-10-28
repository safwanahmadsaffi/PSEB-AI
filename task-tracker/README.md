# Mini Task Tracker

A menu-based Python task tracker for the Week 1, Day 2 mini project. Tasks are stored in `tasks.json`, so they can be loaded again the next time the program runs.

## Features

- Add a task with a non-empty title.
- View all tasks with numbered positions.
- See whether each task is `Pending` or `Done`.
- Mark a task as complete.
- Delete a task.
- Save changes automatically to `tasks.json` after adding, completing, or deleting.
- Load saved tasks automatically when the program starts.
- Handle missing or invalid JSON files, empty titles, invalid menu choices, invalid numbers, and out-of-range task numbers.

## Files

- `mini_task_tracker.py` - the complete Python program.
- `tasks.json` - created automatically when a task is added, completed, or deleted.

## Requirements

- Python 3.8 or newer
- No external packages are required.

## How to run

Open a terminal in this project folder and run:

```bash
python mini_task_tracker.py
```

On some systems, use:

```bash
python3 mini_task_tracker.py
```

Choose an option from the menu:

```text
--- TASK TRACKER ---
1. Add   2. View   3. Complete   4. Delete   5. Exit
Choice:
```

The program creates `tasks.json` in the same folder as the Python script. Because Google Colab runtimes are temporary, download `tasks.json` or save it to Google Drive if you need to keep the data after the runtime ends.

## Example workflow

1. Choose `1` and enter `Read notes`.
2. Choose `2` to see `Read notes [Pending]`.
3. Choose `3`, then enter task number `1`.
4. Choose `2` again to see `Read notes [Done]`.
5. Choose `5` to exit.

## Testing completed

The program was checked for:

- Adding and viewing a task.
- Completing a task and displaying the `Done` status.
- Deleting a task.
- Rejecting a blank title.
- Rejecting an invalid menu choice.
- Rejecting non-numeric and out-of-range task numbers.
- Starting correctly when `tasks.json` does not exist.
- Reloading saved tasks when the program is started again.

## GitHub submission

Create a GitHub repository, then upload `mini_task_tracker.py` and `README.md`. Make at least two meaningful commits, for example:

```bash
git init
git add mini_task_tracker.py README.md
git commit -m "Add task tracker program and documentation"
git add .
git commit -m "Improve validation and persistence handling"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```

Submit the URL of the GitHub repository, not the URL of an individual file.
