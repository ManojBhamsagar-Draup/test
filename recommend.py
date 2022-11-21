import csv


def get_nearby_location(location):
    nearby_location = None
    try:
        with open('location.csv', mode='r') as file:
            # reading the CSV file
            loc_file = csv.DictReader(file)

            # displaying the contents of the CSV file
            for i in loc_file:
                print(i[location])
    except Exception as e:
        print(repr(e))
    return nearby_location

print(get_nearby_location("Sunderland, United Kingdom"))
