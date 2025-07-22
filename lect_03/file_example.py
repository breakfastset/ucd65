
in_file = open("quotes.txt", "r")

print(in_file.read(1))   # read 1 char
print(in_file.read(3))   # read another 3 chars
print("Position in the file:", in_file.tell())

rest_of_line = in_file.readline()  # read 1 line
print(rest_of_line)
print("Position in the file:", in_file.tell())

rest_of_quotes = in_file.read()
print(rest_of_quotes)

more_to_go = in_file.read()    # already at the end of the file
print(f"Any more? [{more_to_go}]")

print("--- Going back to the start of the file ---")
in_file.seek(0)    # go back to the start of the file

for line in in_file:   # print line by line
    print(line)


in_file.close()  # close to release resources