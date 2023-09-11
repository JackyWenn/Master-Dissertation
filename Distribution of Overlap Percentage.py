import csv
import matplotlib.pyplot as plt

# Read the data.csv file
with open('data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    all_data = list(reader)

    # Filter rows where 'Overlap Percentage' is greater than 80%
    high_overlap_data = [row for row in all_data if float(row['Overlap Percentage']) > 80]

# Calculate the percentages
total_count = len(all_data)
high_overlap_count = len(high_overlap_data)
low_overlap_count = total_count - high_overlap_count

# Categories and counts
categories = ['Overlap > 80%', 'Overlap <= 80%']
counts = [high_overlap_count, low_overlap_count]

# Plot the pie chart
plt.figure(figsize=(10, 6))
plt.pie(counts, labels=categories, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Overlap Percentage')
plt.show()