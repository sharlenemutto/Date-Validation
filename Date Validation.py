#This program asks a user to enter a date in DD/MM/YY format.
#It converts the date input to a list and converts the date to month, dd, yyyy
#format.  The year must be two digits and it must be 13.

def main():
    date_string = input('Please enter a date in 2013 using MM/DD/YY format: ')
    #words can also be thought of as list.  Spaces are usually used to split the word string.  Can for split
    #at / by putting it into the bracket
    date_list = date_string.split('/')
    month = int(date_list[0])
    day = int(date_list[1])
    year = int(date_list[2])

    while month > 12 or month < 1: #validate the month
        date_string = input('Invalid month, please enter a valid month. Please re-enter date DD/MM/YY formt: ')
        date_list = date_string.split('/')
        month = int(date_list[0])
        year = int(date_list[2])
        day = int(date_list[1])
    if month == 1 or month == 3 or month == 6 or month == 8 or month == 7 or month == 10 or month == 12:
       while day > 31 or day < 1:
           date_string = input('Invalid day, please enter a valid day.  Re-enter date DD/MM/YY format: ')
           date_list = date_string.split('/')
           year = int(date_list[2])
           month = int(date_list[0])
           day = int(date_list[1])
            
    if month == 2:
        while day > 28 or day < 1: #2013 was not a leap year
            date_string = input('Invalid day, please enter a valid day.  Re-enter date DD/MM/YY format: ')
            date_list = date_string.split('/')
            year = int(date_list[2])
            month = int(date_list[0])
            day = int(date_list[1])
    
    if month == 4 or month == 5 or month == 9 or month == 11:
        while day > 30 or day < 1:
            date_string = input('Invalid day, please enter a valid day.  Re-enter date DD/MM/YY format: ')
            date_list = date_string.split('/')
            year = int(date_list[2])
            month = int(date_list[0])
            day = int(date_list[1])
        
    while year != 13: #validate the year
        date_string = input('Invalid year, please enter 13 for the year. Re-enter date DD/MM/YY format: ')
        date_list = date_string.split('/')
        year = int(date_list[2])
        month = int(date_list[0])
        day = int(date_list[1])
    
    
    #display date where the numeric month is converted to the corresponding month
    print(convert_month(month), day,',',convert_year(year))
    #call the convert_month format
    #call the convert year format
    #to display year as four digits

#function gets number month input and returns month on string format
def convert_month(month):
    if month == 1:
        return 'January'
    if month == 2:
        return 'February'
    if month == 3:
        return 'March'
    if month == 4:
        return 'April'
    if month == 5:
        return 'May'
    if month == 6:
        return 'June'
    if month == 7:
        return 'July'
    if month == 8:
        return 'August'
    if month == 9:
        return 'September'
    if month == 10:
        return 'October'
    if month == 11:
        return 'November'
    if month == 12:
        return 'December'
    
#function converts year '13 to 2013
def convert_year(year):
    year_string = str(year)
    formatted_year = '20' + year_string
    return formatted_year

main()




    
