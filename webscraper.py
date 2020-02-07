import requests
import urllib.request
import time
import re
from bs4 import BeautifulSoup

def download_subject_list():
    subjects = []
    url = "https://studentservices.uwo.ca/secure/timetables/mastertt/ttindex.cfm"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    select = soup.find('select', attrs={'id': 'inputSubject'})
    for option in select.findAll('option'):
        new_subject = option['value']
        if new_subject not in subjects:
            subjects.append(new_subject)

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

def download_subject_data(subject_page):
    cleaned_page = subject_page.replace('\n', '').replace('\t', '')
    soup = BeautifulSoup(cleaned_page, 'html.parser')
    current_object = soup.find("h4")
    current_session = Session

    while current_object != None:
        current_session.course_name = current_object.text
        current_object = current_object.find_next("p")
        
        current_session.course_desc = current_object.text
        current_object = current_object.find_next("table")

        # Here, must parse through each tr to get the data for the course
        session_data = current_object.children
        # Now, parse the tbody
            # Then, parse each row in the tbody

        for row in session_data:
            if row == ' ' or re.match(r'(<thead>)[.\n]*', str(row)):
                continue
            dirty_session = row.contents[1].contents
            session = [i for i in dirty_session if (i != ' ')]
            current_session.section = session[0].text
            current_session.component = session[1].text
            current_session.class_nbr = session[2].text
            current_session.days = session[3].contents
            current_session.start_time = session[4].text
            current_session.end_time = session[5].text
            current_session.location = session[6].text
            current_session.instructor = session[7].text.strip('\r ')

        current_object = current_object.find_next("h4")

download_subject_list()
actursci_page = download_subject_page("ACTURSCI")
download_subject_data(actursci_page)