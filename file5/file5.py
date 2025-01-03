import csv

# A list of dictionaries
mydict = [
    {"first": "Harry", "last": "Potter"},
    {"first": "Ron", "last": "Weasely"}, 
    {"first": "Hermione", "last": "Granger"}
]

# Write the csv file
with open("file5.csv", "w") as file:
    writer = csv.DictWriter(file, fieldnames=["first", "last"])
    writer.writeheader()
    writer.writerows(mydict)
    
    
# Read the file
with open("file5.csv", "r") as csvfile:
    file = csv.DictReader(csvfile)
    for row in file:
        print(row)