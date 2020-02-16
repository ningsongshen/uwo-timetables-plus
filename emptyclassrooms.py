import csv, datetime
classrooms = set()
times = [x/2 for x in range(14, 48)]
usage = {}
sem = 2

for d in ["Mo", "Tu", "We", "Th", "Fr"]:
    usage[d] = {x: set() for x in times}

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

        except ValueError:
            continue
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
# with open('classrooms.csv')

day = input("Enter a day: ")
hope = float(input("Enter a time: "))

print(classrooms.difference(usage[day][hope]))



# Use set intersection, difference to compute available rooms, and use it many times to compute available rooms over many hours, and over different days