str_manip = input("Please enter a sentence: ")
string_length = len(str_manip)
print(f"The length of the string is: {string_length}")
last_letter = str_manip[-1]
modified_str = str_manip.replace(last_letter, '@')
print(f"The modified sentence is: {modified_str}")
last_three_reversed = str_manip[:-4:-1]
print(last_three_reversed)

five_letter_word = str_manip[:3] + str_manip[-2:]
print(five_letter_word)
