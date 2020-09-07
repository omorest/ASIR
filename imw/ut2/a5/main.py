import sys


def num_vowels(text):
    vocales = "aeiou"
    num = 0
    for char in text:
        if char.lower() in vocales:
            num += 1

    return num


def num_whitespaces(text):
    num = 0
    for char in text:
        if char == " ":
            num += 1
    return num


def num_digits(text):
    num = 0
    for char in text:
        if char.isdigit():
            num += 1
    return num


def num_digits2(text):
    num = 0
    digits = "0123456789"
    for char in text:
        if char in digits:
            num += 1
    return num


def num_words(text):
    text_list = text.split()
    nw = len(text_list)

    return nw


def num_words2(text):
    text_list = text.split()
    nw = 0
    for char in text_list:
        if char.isdigit() is False:
            nw += 1
    return nw


def reverse(text):
    cant_letras = len(text)
    inv = ""

    for char in range(cant_letras - 1, -1, -1):
        rev = text[char]
        inv += rev
    return inv


def length(text):

    l = len(text)

    return l


def halfs(text):
    size = len(text)
    if size >= 2:
        middle = size // 2
        first_half = text[:middle]
        second_half = text[middle:]

    return " | ".join((first_half, second_half))


def upper_vowels(text):
    vocales = "AEIOU"
    utext = ""
    for char in text:
        if char.upper() in vocales:
            utext += char.upper()
        else:
            utext += char

    return utext


def sorted_by_words(text):
    text_list = text.split()
    list_sorted = sorted(text_list)
    sbw = " ".join(list_sorted)

    return sbw


def length_of_words(text):
    text_list = text.split()
    size_list = []

    for char in text_list:
        size = str(len(char))
        size_list.append(size)
    low = " ".join(size_list)

    return low

text = sys.argv[1]
print("Number of vowels: ", num_vowels(text))
print("Number of whitespaces: ", num_whitespaces(text))
print("Number of digits: ", num_digits(text))
print("Number of digits2: ", num_digits2(text))
print("Number of words: ", num_words(text))
print("Number of words2: ", num_words2(text))
print("Inverse of text: ", reverse(text))
print("Length of text: ", length(text))
print("Halfs of text: ", halfs(text))
print("Text with uppercased vowels: ", upper_vowels(text))
print("Sorted by words: ", sorted_by_words(text))
print("Length of words: ", length_of_words(text))
