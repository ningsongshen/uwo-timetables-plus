import csv, datetime

# all possible classrooms
classrooms = set()

# available half-hour timeslots between 7:00 and 24:00
times = [x/2 for x in range(14, 48)]

# dictioanry that holds all the info on when classes are used
usage = {}
for d in ["Mo", "Tu", "We", "Th", "Fr"]:
    usage[d] = {x: set() for x in times}

# short function converts the time (e.g. 8:30 AM) to an int (8.5) that is used in categorizing classrooms
def string_to_int(time_string):
    separator = time_string.index(":")
    space = time_string.index(" ")
    hour = int(time_string[:separator])
    minute = int(time_string[separator+1:space])
    half = False
    meridiem = time_string[space+1:]

    if meridiem == "PM" and hour != 12:
        hour += 12
    if minute == 30:
        half = True

    if half == True:
        return hour + 0.5
    else:
        return hour

# actual classification starts here, with data being pulled from csv file
with open('data/allsem.csv', 'r', newline='') as csvfile:
    freader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in freader:
        try:
            code = row[0]
            day_string = row[6]
            start_string = row[7]
            end_string = row[8]
            start_time = string_to_int(start_string)
            end_time = string_to_int(end_string)
            location_string = row[9]
            classrooms.add(location_string[:-1])

        # some have missing values
        except ValueError:
            continue

        # here, calculate all the half-hour timeslots that the class spans
        # add to a list
        spanning_times = [end_time]
        end = False
        while not end:
            end_time -= 0.5
            spanning_times.append(end_time)
            if end_time == start_time:
                end = True
        
        # if course is not in first sem, skip it
        if code in ["A", "F", "L", "Q", "R", "U", "W", "Y", "Z"]:
            continue


        # for each day that the class takes place, add to each timeslot's set the classroom to indicate it's being used
        if "Mo" in day_string:
            for i in spanning_times:
                usage["Mo"][i].add(location_string[:-1])
        if "Tu" in day_string:
            for i in spanning_times:
                usage["Tu"][i].add(location_string[:-1])
        if "We" in day_string:
            for i in spanning_times:
                usage["We"][i].add(location_string[:-1])
        if "Th" in day_string:
            for i in spanning_times:
                usage["Th"][i].add(location_string[:-1])
        if "Fr" in day_string:
            for i in spanning_times:
                usage["Fr"][i].add(location_string[:-1])

# After processing: here is the interface. Users specify day, start time, end time and it will output all classrooms
# which are empty for the entire duration
day = input("Enter a day: ")
hope_start = float(input("Enter a start time: "))
hope_finish = float(input("Enger an ending time: "))

empty = classrooms
end = False
filled = usage[day][hope_finish]

# start at end, add classrooms for each half hour earlier.
while not end:
    hope_finish -= 0.5
    filled = filled.union(usage[day][hope_finish])
    if hope_finish == hope_start:
        end = True
    
# find the difference between the available classrooms and the used classrooms, which should be the available classrooms!
print(classrooms.difference(filled))


# Old Steps:
# Use set intersection, difference to compute available rooms, and use it many times to compute available rooms over many hours, and over different days

# Next Steps:
# A visual chart. Take my favourite classrooms, and see when they're available.
# Statistics on UWO classroom utilization
# See which classrooms are available on a consistent basis, i.e. they are available at the same time everyday.