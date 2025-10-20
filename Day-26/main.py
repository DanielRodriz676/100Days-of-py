# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

name = 'DANIEL'

nato = pandas.read_csv('Day-26/nato_phonetic_alphabet.csv')

nato_name3 = {l_name:[arrow.code for (index, arrow) in nato.iterrows() if arrow.letter in l_name] for l_name in name}

nato_name = {l_name:{row.letter: row.code for (index, row) in nato.iterrows()}[l_name] for l_name in name}

print(nato_name)

































