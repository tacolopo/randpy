# Use a Python string method to prove which of the following files
# are .pdf files, and which aren't.
# Call the method on each file string and print() Python's response.

file_1 = "operators.pdf"
file_2 = "snowfall.jpg"
file_3 = "uncle-joes-wedding.doc"
file_4 = "invitation.pdf"

if file_1.endswith('.pdf'):
    print(file_1)
else:
    print(file_1, ' is not a .pdf')
if file_2.endswith('.pdf'):
    print(file_2)
else:
    print(file_2, ' is not a .pdf')
if file_3.endswith('.pdf'):
    print(file_3)
else:
    print(file_3, ' is not a .pdf')
if file_4.endswith('.pdf'):
    print(file_4)
else:
    print(file_4, ' is not a .pdf')