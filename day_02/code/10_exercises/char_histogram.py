# Install matplot lib
# in command prompt -> pip install matplotlib

# Create a character histogram
import matplotlib.pyplot as plt

# Initialization
chars = 'abcdefghijklmnopqrstuvwxyz'
d = {}
for char in chars:
    d.setdefault(char, 0)

# Input
text = input('Enter text: ')

# Processing
for char in text.lower():
    if(char in chars):
        d[char] = d[char] + 1

# Output
x = list(chars)
y = []
for char in chars:
    y.append(d[char])

plt.bar(x, y, color='r')
plt.show()
