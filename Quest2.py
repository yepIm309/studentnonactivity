counter = 0
string = input("Enter a string ")
print("Line lenght = ", len(string))

for letter in string:
    counter += 1

    if (counter == 3 or letter == string[-1]):
        continue

if letter == 'c':
    print("There is a letter 'C' here")
    print(letter)