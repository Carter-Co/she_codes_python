from datetime import datetime
def convert_mmddyyyy_date(date):
    '''Takes a date in the format mm/dd/yyyy and converts it to a datetime object.

    Args:
        date: string of a date in the mm/dd/yyyy format.

    Returns: a datetime object.
    '''
    return datetime.strptime(date, '%m/%d/%Y')
    
x=convert_mmddyyyy_date("08/07/2021")
print(x)

def read_csv_file(file_name):
    '''Reads a csv file and returns the data as a list.

    Args:
        file_name: a string representing the path and name of a csv file.

    Returns: a list.
    '''
    pass
