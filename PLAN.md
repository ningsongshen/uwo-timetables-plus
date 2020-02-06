# Project Planning

## Contributors

Ningsong Shen

## Inspirations

[NUSMods](https://nusmods.com/)

[UWFlow](https://uwflow.com/)

## Resources

All from Western University:

[Student Centre](https://student.uwo.ca)

[Academic Calendar](http://www.westerncalendar.uwo.ca/)

[Draft My Schedule](https://draftmyschedule.uwo.ca)

[Western Timetables](https://studentservices.uwo.ca/secure/timetables/mastertt/ttindex.cfm)

[Student Questionnaires on Courses and Teaching Results](https://sqct.uwo.ca/)

## Tools

There are a few options here, front-end, back-end, web scraping, any data analytics.

Python, Ruby on Rails, HTML/CSS/JavaScript, SQLite

## Planned Features

This is just a brainstorming dropoff. Eventually, this list will be moved to GitHub Projects to make management easier.

[ ] Timetable optimization (timeslot, location, professor, classroom quality)
[ ] Empty classrooms
[ ] Similar classes (integration with Academic Calendar)
[ ] Professor ratings

## Development Notes

At the top:
form with option for subject. The goal is to loop through each subject to download all the data (there is a max of 600 courses per search)
Structure of an entry:
h4 Course Name
p Course Description
table class="table table-striped" Contains the Data for the courses
Headings: Section, component, class number, days start time, end time, location, instructor, requisites and constraints, status
parse the table

Process Flow:
Get List of Subjects
For each Subject, get the page data
    Get the course data
    Pandas

End goal: write to a csv or json file.

Then, design an interface that will find all life optimizations as noted above

## Known Issues

Please put them in GitHub Issues. This will streamline the bug-fixing process.
