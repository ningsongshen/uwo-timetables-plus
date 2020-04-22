import csv, datetime
import pandas as pd

while True:
    classroom = input("Enter a classroom: ")

    # available half-hour timeslots between 7:00 and 24:00
    times = [(x / 2) for x in range(14, 48)]

    # dictionary that holds all the info on when classes are used
    usage = {}
    usage_blocks = 0
    for d in ["Mo", "Tu", "We", "Th", "Fr"]:
        usage[d] = {x: " " for x in times}

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
                location_string = row[9][:-1]

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
            
            # if course is not in first sem or wrong classroom, skip it
            if code in ["A", "F", "L", "Q", "R", "U", "W", "Y", "Z"]:
                continue
            if location_string != classroom:
                continue

            # for each day that the class takes place, add to each timeslot's set the classroom to indicate it's being used
            if "Mo" in day_string:
                for i in spanning_times:
                    usage["Mo"][i] = "X"
                    usage_blocks += 1
            if "Tu" in day_string:
                for i in spanning_times:
                    usage["Tu"][i] = "X"
                    usage_blocks += 1
            if "We" in day_string:
                for i in spanning_times:
                    usage["We"][i] = "X"
                    usage_blocks += 1
            if "Th" in day_string:
                for i in spanning_times:
                    usage["Th"][i] = "X"
                    usage_blocks += 1
            if "Fr" in day_string:
                for i in spanning_times:
                    usage["Fr"][i] = "X"
                    usage_blocks += 1


    df = pd.DataFrame(usage)
    print(df)
    print("Classtime Utilization:", str(round(usage_blocks/142*100, 3))+"%")
    print("24h Utilization:", str(round(usage_blocks/240*100, 3))+"%")
