
my_string = input("Введите текст: ")
print(len(my_string))
print(my_string.upper())
print(my_string.lower())
my_string_no_spaces = my_string.replace(" ", "")
print(my_string_no_spaces)
if my_string:
    print(my_string[0])
else:
    print()
if my_string:
    print(my_string[-1])
else:
    print()