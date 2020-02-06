import requests
import urllib.request
import time
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
    print(subjects)

def download_subject_data(subject):
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

download_subject_list()