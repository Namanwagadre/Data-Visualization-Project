
import matplotlib.pyplot as pt
import csv

# Initialize empty dictionary to store data
data = {}

# Read data from CSV file
with open('job_salary.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header if exists
    for i in reader:
        label = i[7]  # Assuming first column contains labels
        value =(i[4])  # Assuming second column contains values
        data[label] = value
        print(i)

# Plotting the pie graph
labels = data.keys()
sizes = data.values()

pt.pie(sizes, labels=labels, autopct='%1.1f%%')
pt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
pt.title('percentage of experience level')
pt.legend(loc=3)
pt.show()
