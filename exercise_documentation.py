import pandas as pd

def x(a, print_columns=False):
""" 
It parses an excel file and returns a list containing column headers.

args:
    a (String): String containing the path to an excel file.
    print_columns (Bool): If true, the method prints the header of each column of file a. Default: False.
    
returns:
    column_headers (list): A list containing all column headers in an excel file.
"""
   b = pd.read_excel(a)
   column_headers = list(b.columns.values)
   if print_columns:
       print("\n".join(column_headers))
   return column_headers
