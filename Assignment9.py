import csv
import json

# Create CSV file
with open("students.csv", "w", newline="") as f:
    f.write("id,name,department,marks\n")
    f.write("1,Aditi Sharma,Computer Science,88\n")
    f.write("2,Rahul Verma,Mechanical,76\n")
    f.write("3,Sneha Iyer,Electronics,92\n")


# Read CSV file
with open("students.csv", "r", newline="") as f:
    reader = csv.DictReader(f)
    data = list(reader)


# Convert CSV data to JSON
with open("students.json", "w") as f:
    json.dump(data, f, indent=4)


print("CSV data:")
for row in data:
    print(row)

print("\nData converted successfully!")
print("JSON file created: students.json")