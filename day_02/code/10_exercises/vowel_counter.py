# Program to find the number of vowel occurances

# input

text = input('Enter some text: ')

# process

vowelStr = 'aeiou'
vowelDict = {}
for vowel in vowelStr:
    vowelDict.setdefault(vowel, text.lower().count(vowel))

# output
print('-'*15)
print('Vowel'.ljust(6), '| ',  'Count')
print('-'*15)
for key, value in vowelDict.items():
    print(key.ljust(6), '| ',  value)
print('-'*15)
