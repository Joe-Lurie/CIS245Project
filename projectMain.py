# commitment.py - Step 1: what a commitment looks like

CATEGORIES = ["class", "assignment", "event", "chore", "work", "practice", "other"]
PRIORITIES = ["low", "medium", "high"]

# One commitment = one dictionary
example = {
    "id": 1,
    "name": "CIS 245 Lecture",
    "date": "2026-10-05",    # YYYY-MM-DD
    "start": "10:00",        # 24-hour HH:MM
    "end": "11:00",
    "category": "class",
    "priority": "high",
    "notes": "Room 120",
}

# The whole schedule = a list of these dictionaries
def sample_schedule():
    return [
        {"id": 1, "name": "CIS 245 Lecture", "date": "2026-10-05", "start": "10:00", "end": "11:00",
         "category": "class", "priority": "high", "notes": ""},
        {"id": 2, "name": "Soccer Practice", "date": "2026-10-05", "start": "09:00", "end": "11:00",
         "category": "practice", "priority": "medium", "notes": "overlaps lecture"},
        {"id": 3, "name": "Accounting HW 3", "date": "2026-10-07", "start": "23:00", "end": "23:59",
         "category": "assignment", "priority": "high", "notes": ""},
    ]