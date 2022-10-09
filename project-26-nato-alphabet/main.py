import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word. ").upper()


phonetic_list = [phonetic_dict[letter] for letter in word]
print(phonetic_list)
