from cs50 import get_string


def main():
    s = get_string("Insert String: ")

    letters = count_letters(s)
    words = count_words(s)
    sentences = count_sentences(s)

    index = 0

    st = 100 * float(sentences) / float(words)
    l = 100 * float(letters) / float(words)

    index = 0.0588 * l - 0.296 * st - 15.8

    # round index

    indexr = round(index)

    if (indexr >= 16):
        print("Grade 16+")

    elif (indexr < 1):
        print("Before Grade 1")

    else:
        print(f"Grade {indexr}")  # Using string interpolation


def count_letters(text):
    countL = 0
    for char in text:
        if (char.isalpha()):  # Check if each character is alphabetical
            countL += 1
    return countL


def count_words(text):
    countW = 1  # Assuming will always have one word

    for char in text:
        if (char.count(" ")):  # using count functin to look out for spaces
            countW += 1
    return countW


def count_sentences(text):
    countST = 0

    for char in text:
        if (char == "!" or char == "?" or char == "."):  # check if each character of the string is an sentence
            countST += 1
    return countST


main()