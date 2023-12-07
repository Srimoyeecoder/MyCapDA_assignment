# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 20:19:37 2023

@author: SRIMOYEE
"""

import matplotlib.pyplot as plt

# Hypothetical data: Productivity levels and times of the day
time_of_day = ['Morning', 'Afternoon', 'Evening', 'Night']
productivity_levels = [4, 3, 5, 2]  

# Creating a bar graph
plt.bar(time_of_day, productivity_levels, color='green')
plt.xlabel('Time of the Day')
plt.ylabel('Productivity Level (1-5)')
plt.title('Bivariate Analysis: Time of the Day vs Productivity')
plt.ylim(0, 5)  

# Display the plot
plt.show()
