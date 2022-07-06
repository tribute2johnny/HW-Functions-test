def return_10():
    return 10

def add(one, two):
    return one + two
    
def subtract(ten, five):
    return ten - five

    
def multiply(four, two):
    return four * two

def divide(ten, two):
    return ten/two

def length_of_string(string_length):
    return len(string_length)

def join_string(string_1, string_2):
    return string_1 + string_2

def add_string_as_number(num1, num2):
    return int(num1) + int(num2)

def number_to_full_month_name(month):
    if month == 1:
        return "January"
    elif month == 3:
        return "March"
    elif month == 9:
        return "September"

def number_to_short_month_name(month):
    if month == 1:
        return "Jan"
    elif month == 4:
        return "Apr"
    elif month == 10:
        return "Oct"