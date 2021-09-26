def my_function(x = 0):
    return lambda x : x + 1

value = my_function()

print(value(2))