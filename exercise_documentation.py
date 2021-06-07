import pandas as pd

def get_spreadsheet_columns(file_loc, print_columns=False):
""" 
It parses an excel file and returns a list containing column headers.

args:
    file_loc (String): String containing the path to an excel file.
    print_columns (Bool, optional): If true, the method prints the header of each column of file a. Default: False.
    
returns:
    column_headers (list): A list containing all column headers in an excel file.
"""
   speadsheet_info = pd.read_excel(file_loc)
   column_headers = list(speadsheet_info.columns.values)
   if print_columns:
       print("\n".join(column_headers))
   return column_headers
