# uwo-timetables-plus

An improvement over the existing timetable interface with more data and visualization options.

## Inspirations

Data scraper source: <https://github.com/shrumit/timetable-scraper-java>

Sample timetable generator: <https://github.com/shrumit/Western-Timetable-Maker>

Both are great, but miss some features that I want.

My preferred functionality: find when and where the empty classrooms are, optimal class timings, prof info...

## Updating the raw data

1. webscraper (be careful for the request limit/bot blocking)
2. merge csv files into one file
3. findsemester
4. emptyclassrooms

## Usage

Use pipenv to install all dependencies

```python
pipenv shell
python emptyclassrooms.py
```

- Days of the week: first two letters only.
- Start time: 24 hours clock, use .5 for the half hour. Ex: 3:30 is 15.5
- End time: same format, do not enter the same time
- Returns a list of classrooms without a scheduled class at that time

```python
python favclassrooms.py
```

- Enter a classroom code: building-number. Ex: WSC-240, UC-9999
- Prints out a chart of when it is being used
- Displays utilization rate
