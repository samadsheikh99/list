# Define functions for each data type
def function_for_list(data):
    return [x * 2 for x in data]

def function_for_dict(data):
    return {key: value * 2 for key, value in data.items()}

def function_for_set(data):
    return {x * 2 for x in data}

def function_for_tuple(data):
    return tuple(x * 2 for x in data)

# Create a dictionary with functions for each data type
data_functions = {
    'list': function_for_list,
    'dict': function_for_dict,
    'set': function_for_set,
    'tuple': function_for_tuple
}

# Test data
sample_list = [1, 2, 3, 4]
sample_dict = {'a': 1, 'b': 2, 'c': 3}
sample_set = {1, 2, 3, 4}
sample_tuple = (1, 2, 3, 4)

# Apply functions to the data
result_list = data_functions['list'](sample_list)
result_dict = data_functions['dict'](sample_dict)
result_set = data_functions['set'](sample_set)
result_tuple = data_functions['tuple'](sample_tuple)

# Print the results
print("Original List:", sample_list)
print("Result List:", result_list)

print("Original Dictionary:", sample_dict)
print("Result Dictionary:", result_dict)

print("Original Set:", sample_set)
print("Result Set:", result_set)

print("Original Tuple:", sample_tuple)
print("Result Tuple:", result_tuple)




