# Write a function that, depending on the first line of the input, reads one of the following strings:"int","real", or "string".
# If the data type is an int, multiply the number by 2.
# If the data type is real, multiply the number by 1.5 and format the result to the second decimal point.
# If the data type is a string, surround the input with "$".


def check_data(input_type, input_data):
    if input_type == "int":
        input_data = int(input_data)
        multiply_int = input_data * 2
        return multiply_int
    if input_type == "real":
        input_data = float(input_data)
        multiply_float = input_data * 1.50
        return f"{multiply_float:.2f}"
    if input_type == "string":
        input_data = "$" + input_data + "$"
        return input_data



type_of_input = input()
input_data_type = input()
result = check_data(type_of_input, input_data_type)
print(result)