# Here is a Python script that reads the `cricket_scores.csv` file and plots the number of runs scored over time using matplotlib:

#```python
import pandas as pd
import matplotlib.pyplot as plt
import pdb

# Read the CSV file
csv_file = 'cricket_scores.csv'
data = pd.read_csv(csv_file, on_bad_lines='skip')
#pdb.set_trace()

# Convert the 'Date' column to datetime format
data['Date'] = pd.to_datetime(data['Date'], format='%dth %B %Y', errors='coerce')

# Drop rows with invalid dates
data.dropna(subset=['Date'], inplace=True)

# Sort the data by date
data.sort_values('Date', inplace=True)

# Plot the number of runs scored over time
plt.figure(figsize=(10, 6))
plt.plot(data['Date'], data['Runs Scored'], marker='o', linestyle='-', color='b')
plt.title('Number of Runs Scored Over Time')
plt.xlabel('Date')
plt.ylabel('Runs Scored')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot as an image file
plt.savefig('runs_scored_over_time.png')

# Display the plot
#plt.show()


# Plot wickets taken over time
plt.figure(figsize=(10,6))
plt.plot(data['Date'], data['Wickets'], marker='o', linestyle='-', color='g')
plt.title('Number of wickets taken')
plt.xlabel('Date')
plt.ylabel('Wickets taken')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# save plot
plt.savefig('wickets_over_time.png')

#```

#This script does the following:
#1. Reads the `cricket_scores.csv` file into a pandas DataFrame.
#2. Converts the 'Date' column to datetime format and drops rows with invalid dates.
#3. Sorts the data by date.
#4. Plots the number of runs scored over time using matplotlib.
#5. Saves the plot as an image file (`runs_scored_over_time.png`).
#6. Displays the plot.

#Make sure to have the necessary libraries installed:
#```bash
#pip install pandas matplotlib
#```
