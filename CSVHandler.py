import csv
import os
import matplotlib.pyplot as plt
from datetime import datetime

class CSVHandler:
    def __init__(self, file_name, col1_name, col2_name):
        self.file_name = file_name
        self.col1_name = col1_name
        self.col2_name = col2_name
        self.data = []
        
        # Create CSV file with headers if it doesn't exist
        if not os.path.isfile(self.file_name):
            with open(self.file_name, 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=[self.col1_name, self.col2_name])
                writer.writeheader()

    def insert_data(self, data):
        with open(self.file_name, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=[self.col1_name, self.col2_name])
            writer.writerow({self.col1_name: data[0], self.col2_name: data[1]})
        self.data.append(data)

    def retrieve_data(self):
        with open(self.file_name, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            retrieved_data = []
            for row in reader:
                retrieved_data.append((row[self.col1_name], row[self.col2_name]))
        return retrieved_data
    def plot_data(self):
        data = self.retrieve_data()
        x_values = []
        y_values = []

        # Filter out rows with missing or invalid values
        for row in data:
            if row[0] and row[1].strip() != '' and row[1].replace('.', '').isdigit():
                x_values.append(row[0])
                y_values.append(float(row[1]))

        plt.plot(x_values, y_values)
        plt.xlabel(self.col1_name)
        plt.ylabel(self.col2_name)
        plt.title("Plot of {} vs {}".format(self.col1_name, self.col2_name))
        plt.savefig('templates/fig.png')
        



    def clear_data(self):
        with open(self.file_name, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=[self.col1_name, self.col2_name])
            writer.writeheader()
        self.data = []