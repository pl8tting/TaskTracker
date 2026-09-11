
# TaskTracker

A desktop task management application built with Python and Tkinter. The application allows users to organize tasks into categories, move tasks between categories, and save their tasks locally between sessions.

The interface is styled using the [Sun Valley ttk theme](https://github.com/rdbende/Sun-Valley-ttk-theme) by rdbende.

## Screenshot
<img width="447" height="325" alt="Screenshot 2026-09-11 211729" src="https://github.com/user-attachments/assets/c64502a3-7ada-45fd-8927-d6d005cd410a" />
 
## Features

- Add new tasks
- Organize tasks into Not Done, Completed, and Long Term categories
- Move tasks between categories
- View tasks in a tree-based interface
- Save tasks locally using JSON
- Automatically load saved tasks when the application starts

## How It Works

Tasks are organized into three categories: Not Done, Completed, and Long Term.

Users can add new tasks and move them between categories using the graphical interface. Tasks are displayed in a tree-based view and stored locally in a JSON file.

When the application starts, previously saved tasks are loaded automatically. Changes are saved when the application closes so tasks remain available between sessions.

## Usage

Run the application with:

```bash
python schedule.py
```
