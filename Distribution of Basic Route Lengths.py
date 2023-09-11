import csv
import matplotlib.pyplot as plt

# Read the data.csv file and get the 'Basic Route Length' values
with open('data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    lengths = [float(row['Basic Route Length']) for row in reader]

# Categorize the lengths into different ranges
categories = ['300-1000', '1000-2000', '2000-3000', '3000+']
counts = [0, 0, 0, 0]

for length in lengths:
    if 300 <= length < 1000:
        counts[0] += 1
    elif 1000 <= length < 2000:
        counts[1] += 1
    elif 2000 <= length < 3000:
        counts[2] += 1
    else:
        counts[3] += 1

# Plot the pie chart
plt.figure(figsize=(10, 6))
plt.pie(counts, labels=categories, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Basic Route Lengths')
plt.show()