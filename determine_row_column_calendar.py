import datetime

# This will determine the row and column of any date in a calendar.
# The Rows and Columns of the calendar start with 1 and not 0.

def determine_row_column(date_as_str):
    today_in_datetime = datetime.datetime.strptime(date_as_str, "%d %b %Y")
    weekday_of_today = today_in_datetime.weekday()
     # Converting pairing so that column starts on Sunday not Monday as datetime.weekday starts on Monday.
    weekday_pairing = {0: 2, 1: 3, 2: 4, 3: 5, 4: 6, 5: 7, 6: 1}
    column = weekday_pairing[weekday_of_today]
    first_day_as_int = 1
    today_as_int = int(date_as_str[0:2])
    row = 1
    previous_column = 0
    # Go through each day in the calendar and determine it's column and then increase rows if you hit a Sunday.
    # TODO: I'm certain this can be optimized.
    for x in range(first_day_as_int, today_as_int+1):
        if x < 10:
            day = "0"+f"{x}"
        else:
            day = str(x)
        date_as_str = date_as_str.replace(date_as_str[0:2], day, 1)
        today_in_datetime = datetime.datetime.strptime(date_as_str, "%d %b %Y")
        weekday_of_today = today_in_datetime.weekday()
        current_column = weekday_pairing[weekday_of_today]
        if current_column == 1 and previous_column > 0:
            row +=1
        else:
            pass
        if current_column == 7:
            previous_column +=1
    return row, column
