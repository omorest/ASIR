import sys

sentence = sys.argv[1]


def count_words(sentence):
    summary = {}
    sentence_list = sentence.split()
    for char in sentence_list:
        num = 1
        if char in summary:
            summary[char] = num + 1
        else:

            summary[char] = num

    return summary

for key, value in (count_words(sentence)).items():
    print(key, ":", value)
