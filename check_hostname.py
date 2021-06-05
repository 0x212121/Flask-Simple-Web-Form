import csv

def checkhostname(hostname):    
    ix = hostname.upper()
    with open('workstation_type.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if ix == row[0]:
                return row[1]
    return 'UNKNOWN'