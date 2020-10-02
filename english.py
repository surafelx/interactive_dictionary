import json
import difflib
from difflib import get_close_matches

data = json.load(open("C:/Users/suraf/OneDrive/Desktop/python projects/projects/a-english-dictionary/data.json"))

while True:
    inputWord = input("Enter a word to define: ")
    if inputWord.lower() in data:
      print("\n".join(data[inputWord.lower()]))
    elif len(get_close_matches(inputWord.lower(), data.keys())) > 0:
        for i in get_close_matches(inputWord.lower(), data.keys()):
            checkWord = input(f"Did you mean {i} ... Y or N? ")
            if checkWord == "Y":
                print("\n".join(data[i]))
                break
            elif checkWord == "N": 
                continue
    else: 
       print("The word doesn't exist. Try again.")