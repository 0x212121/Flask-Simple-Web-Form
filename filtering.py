import re
import csv

def filter_type(hostname):    
    ix = hostname.upper()
    with open('workstation_type.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if ix == row[0]:
                return row[1]
    return 'UNKNOWN'

def filter_hostname(hostname):
    check_input = re.match("^[a-zA-Z]{4}\-\w{4}\-\w{4}[a-zA-Z]$", hostname)
    return check_input

def filter_badge(badge_no):
    check_input = re.match("^[UZ]*[0-9]{5,6}$", badge_no)
    return check_input