dict = {}

name = input("Enter friends name: ")
lang = input("Enter friends favorite language: ")
dict.update({name: lang})

name1 = input("Enter friends name: ")
lang1 = input("Enter friends favorite language: ")
dict.update({name1: lang1})

name2 = input("Enter friends name: ")
lang2 = input("Enter friends favorite language: ")
dict.update({name2: lang2})

name3 = input("Enter friends name: ")
lang3 = input("Enter friends favorite language: ")
dict.update({name3: lang3})

print(dict) # {'name': 'lang'}