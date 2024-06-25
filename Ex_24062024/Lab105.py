"""letters= ['a','b','c','d','e','i','o','u','z']


def letters_vowel(letters):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return letters in vowels

new_letters_vowels = filter(letters_vowel, letters)
print(list(new_letters_vowels))"""

letters_tuple= ('a','b','c','d','e','i','o','u','z')


def letters_vowel(letters_tuple):
    vowels = ('a', 'e', 'i', 'o', 'u')
    return letters_tuple in vowels

new_letters_vowels = filter(letters_vowel, letters_tuple)
print(tuple(new_letters_vowels))