import json
from difflib import get_close_matches

data = json.load(open(r"C:\Users\NikoDigi\Desktop\Int dictionary\My_dict\1.2 data.json"))

def Dictionary(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif get_close_matches(word,data.keys())[0]:
        yn = input("Do you mean %s?,yes or no:" %get_close_matches(word,data.keys())[0])
        if yn== "yes":
            return data[get_close_matches(word,data.keys())[0]]
        elif yn=="no":
            return "Word does not exist,please try  again."
        else:
            return "we didn't understand your entry"
    else:
        return "Word does not exist,please try  again."
word = input("Provide a word:")
print("" "\n".join(Dictionary(word)))



