# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 19:48:16 2023

@author: SRIMOYEE
"""

# Define two sets
E = {0, 2, 4, 6, 8}
N = {1, 2, 3, 5, 8}

# Perform set operations
union_result = E.union(N)
intersection_result = E.intersection(N)
difference_result = E.difference(N)
symmetric_difference_result = E.symmetric_difference(N)

# Print the results
print(f"Union of E and N is {union_result}")
print(f"Intersection of E and N is {intersection_result}")
print(f"Difference of E and N is {difference_result}")
print(f"Symmetric difference of E and N is {symmetric_difference_result}")
