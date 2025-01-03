import csv
with open("file4.csv","r") as csvfile:
    reader = csv.reader(csvfile)
    # file = next(reader) - to skip first row and start from next
    n = int(input("Enter the specific columns of your choice: "))
    col = []
    for row in reader:
        col.append(row[n])
    print(col)