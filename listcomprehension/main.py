'''with open("./File/List1.txt") as file1:
    file1_data = file1.readlines()
with open("./File/List2.txt") as file2:
    file2_data = file2.readlines()
result = [int(num) for num in file1_data if num in file2_data]
print(result)'''


import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)
word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)