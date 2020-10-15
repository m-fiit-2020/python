s = 'Hello world'
for letter in s.lower():
    if letter in 'aeiouy':
        print(letter.upper(), end='')
        continue
    print(letter, end='')
print(s1)
