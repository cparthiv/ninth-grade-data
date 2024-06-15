def count_columns(input_string):
    elements = input_string.split(',')
    return len(elements)


input_string = input("Enter a comma-separated string: ")
print(count_columns(input_string=input_string))
