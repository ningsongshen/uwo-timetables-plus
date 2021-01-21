# uwo-timetables-plus

Find empty classrooms to study in...as a group or by yourself--with no sound restrictions.

## Background

There are many existing tools out there that solve certain timetable problems:
- Parse the timetables website (old): <https://github.com/shrumit/timetable-scraper-java>
- Generate optimal timetables: <https://github.com/shrumit/Western-Timetable-Maker>
- Many default tools available from the university itself.

All are great, but miss some features that I want. My preferred functionality in this use case is to find when my favourite classrooms are empty, or which classrooms are free at a given time.

## Updating the raw data

1. scraper (be careful for the request limit/bot blocking)
2. merge csv files into one file
3. findsemester
4. emptyclassrooms

## Usage

Use pipenv to install all dependencies

```python
pipenv shell
python emptyclassrooms.py
```

Necessary abbreviations when searching:
- Days of the week: first two letters only.
- Start time: 24 hours clock, use .5 for the half hour. Ex: 3:30 is 15.5
- End time: same format, do not enter the same time
- Returns a list of classrooms without a scheduled class at that time

```python
python favclassrooms.py
```

Necessary abbreviations when searching:
- Enter a classroom code: building-number. Ex: WSC-240, UC-9999
- Prints out a chart of when it is being used
- Displays utilization rate
