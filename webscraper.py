import requests
import urllib.request
import time
import re
import csv
import os
import random
from bs4 import BeautifulSoup

def download_subject_list():
    subjects = []
    url = "https://studentservices.uwo.ca/secure/timetables/mastertt/ttindex.cfm"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    select = soup.find('select', attrs={'id': 'inputSubject'})
    for option in select.find_all('option'):
        new_subject = option['value']
        if new_subject not in subjects and new_subject != '':
            subjects.append(new_subject)
    with open('subjects.txt', 'w') as f:
        for subject in subjects:
            f.write("%s\n" % subject)
    return subjects

def download_subject_page(subject):
    url = "https://studentservices.uwo.ca/secure/timetables/mastertt/ttindex.cfm"
    payload_tuples = [
        ("subject", subject),
        ("Designation", "Any"),
        ("catalognbr", ""),
        ("CourseTime", "All"),
        ("Component", "All"),
        ("time", ""),
        ("end_time", ""),
        ("day", "m"),
        ("day", "tu"),
        ("day", "w"),
        ("day", "th"),
        ("day", "f"),
        ("Campus", "Any"),
        ("command", "search")
    ]
    response = requests.post(url, data=payload_tuples)
    return response.text

def clean_subject_page(page):
    page = page.replace("\n", "").replace("\r", "").replace("\t", "")
    page = page[page.find("<h4>"):]
    soup = BeautifulSoup(page, 'html.parser')

class Session:
    course_name = ""
    course_desc = ""
    section = 1
    component = "LEC"
    class_nbr = 0
    days = "MWF"
    start_time = "8:30"
    end_time = "9:30"
    location = ""
    instructor = ""

    def session_list(self):
        return [self.course_name, self.course_desc, self.section, self.component, self.class_nbr, self.days, self.start_time, self.end_time, self.location, self.instructor]

def convert_to_weeks(week_table):
    soup = BeautifulSoup(week_table, 'html.parser')
    weeks = ""
    current_object = soup.find("td")

    while current_object != None:
        weeks += current_object.text
        current_object = soup.find("td")
    
    return weeks

def download_subject_data(subject_page, subject_name):
    cleaned_page = subject_page.replace('\n', '').replace('\t', '').replace('\r', '').replace('&nbsp;', '')
    soup = BeautifulSoup(cleaned_page, 'html.parser')
    current_object = soup.find("h4")
    
    sessions = []
    while current_object != None:
        course_name = current_object.text
        current_object = current_object.find_next("p")
        
        course_desc = current_object.text
        current_object = current_object.find_next("table")

        # Here, must parse through each tr to get the data for the course
        session_data = current_object.children
        # Now, parse the tbody
            # Then, parse each row in the tbody

        for row in session_data:
            if row == ' ' or re.match(r'(<thead>)[.\n]*', str(row)):
                continue
            for j in row.contents:
                if j == ' ':
                    continue
                dirty_session = j.contents
                
                session = [i for i in dirty_session if (i != ' ')]

                current_session = Session()
                current_session.course_name = course_name
                current_session.course_desc = course_desc
                current_session.section = session[0].text
                current_session.component = session[1].text
                current_session.class_nbr = session[2].text
                current_session.days = session[3].text.replace(' ', '').replace('M', 'Mo').replace('W', 'We').replace('F', 'Fr')
                current_session.start_time = session[4].text
                current_session.end_time = session[5].text
                current_session.location = session[6].text
                current_session.instructor = session[7].text.strip('\r ')

                sessions.append(current_session.session_list())


        current_object = current_object.find_next("h4")
        outname = 'data/' + i + '.csv'
        with open(outname, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(sessions)


# subject_list = download_subject_list()
with open("subjects.txt", "r") as f:
    for i in range(26):
        next(f)
    for j in f:
        i = j.strip("\n")
        time.sleep(random.randint(5, 10))
        page = download_subject_page(i)
        download_subject_data(page, i)
        print(i)
