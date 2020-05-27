import csv

file = open("Phonebook.csv","a")

writer = csv.writer(file)
writer.writerow(("sri","9999"))

file.close