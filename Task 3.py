# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 20:03:38 2023

@author: SRIMOYEE
"""

import matplotlib.pyplot as plt

# Hypothetical data: cycle test marks
cycle_test_marks = {'Test 1': 85, 'Test 2': 78, 'Test 3': 92, 'Test 4': 88, 'Test 5': 95}

# Extracting test names and marks for plotting
test_names = list(cycle_test_marks.keys())
test_marks = list(cycle_test_marks.values())

# Creating a bar plot
plt.bar(test_names, test_marks, color='blue')
plt.xlabel('Cycle Tests')
plt.ylabel('Marks')
plt.title('Cycle Test Marks')
plt.ylim(0, 100)  # Set the y-axis limit to represent percentage marks

# Display the plot
plt.show()
