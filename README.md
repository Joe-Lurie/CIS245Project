Student Calendar & Reminder App

CIS 245 – Group 6: Joseph Lurie, Christian LoGrande, Aidan MacDougall, Drew D'Addio

A Python program that runs in the terminal and helps college students keep track of everything they have to do: classes, assignments, university events, practices, work shifts, and suite/household chores.

What it does (MVP)
Stores commitments. Each one has a name, date, start and end time, category (class, assignment, event, chore, etc.), and priority.
Add, edit, and delete commitments.
Flags conflicts when two commitments overlap, and names both of them.
Shows the week: everything scheduled for the current week, sorted by day and time.
Saves and loads your schedule to a file so nothing is lost when the program closes.
Text menu: add / edit / delete / view / save / quit, running until the user quits.

Example
Add a class on Monday from 10–11 a.m., then add practice on Monday from 9–11 a.m. The program flags the overlap and lists both events.

Stretch goal

Suggest study blocks in the student's free time, based on upcoming assignment deadlines and how long each assignment should take.

Scope
Plain Python only: no external APIs or heavy libraries.
Code is shared through this GitHub repo.
Team roles
Member	Role	Steps
Joseph Lurie	Data & Storage Lead	1, 4, 9 (data side)
Christian LoGrande	Core Logic Lead	2, 3, 5
Aidan MacDougall	Interface & Integration Lead	6, 7
Drew D'Addio	Testing, Documentation & Presentation Lead	8, 10, 9 (support)
Running it
python main.py