# reading the text file
with open("binarycity.txt") as file:
	text = file.read()

# first I tried to figure out what is the encoding of the text

# I collected all the characters present in the text
chars = []
for char in text:
	if char not in chars:
		chars.append(char)

# then I filtered out the letters from A-z and digits from 0-9
import string
ignore = string.ascii_lowercase + string.ascii_uppercase + string.digits
filtered = [c for c in chars if c not in ignore]

# then I saw that the only characters left are '/' and '+' besides the line break character
# I searched the internet then I found this Stack Overflow https://stackoverflow.com/questions/11449577/why-is-base64-encode-adding-a-slash-in-the-result
# I read it and found out that the text is encoded in base64
# then I searched what is a base64 encoding
# base64 is a binary-to-text encoding and it represents binary data in an ascii string format

# and finally, I decoded it using the built-in 'base64' module of Python
import base64
binary = base64.b64decode(text)

# then I saved it into a jpeg file format
with open("binarycity.jpg", "wb") as file:
	file.write(binary)
