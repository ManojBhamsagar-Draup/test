import csv

# opening the CSV file
with open('ML_Synon_Skill_Schema.csv', mode='r') as file:
    # reading the CSV file
    csvFile = csv.DictReader(file)
    # displaying the contents of the CSV file
    for lines in csvFile:
        print(lines)
