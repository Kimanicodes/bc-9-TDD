def super_sum(*args):  # using args for the function
    """Super Sum: A function that adds numbers in list and as integers"""
    total_list = 0
    total_int = 0
    for argument in args:
        if type(argument) is list:
            for number in argument:
                if type(number) is int:
                        total_list = total_list + number
                else:
                    return "Your list has non integer items"
        else:
            if type(argument) is int:
                total_int = total_int + argument
            else:
                return None
    total = total_int + total_list
    return total
