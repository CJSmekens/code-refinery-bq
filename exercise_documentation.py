import pandas as pd

def x(a, print_columns=False):
""" 
Print column headers of excel file

Args:
  a (pandas.String): path to excel file
  print_columns (boolian): True/False
  
Returns:
  list containing the column headers
"""
   b = pd.read_excel(a)
   column_headers = list(b.columns.values)
   if print_columns:
       print("\n".join(column_headers))
   return column_headers
