
sentences = input("Enter a sentence: ")

words = sentences.split()
word_count = len(words)


def count_vowels(sentence):
    vowels = "aeiouAEIOU"
    count = 0

    for char in sentence:
        if char in vowels:
            count += 1

    return count


def count_consonants(sentence):
    vowels = "aeiouAEIOU"
    count = 0

    for char in sentence:
        if char.isalpha() and char not in vowels:
            count += 1

    return count


def longest_word(sentence):
    words = sentence.split()
    longest = ""

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest


def repetition_of_words(sentence):
    words = sentence.lower().split()
    count = {}

    for word in words:
        word = word.strip(".,!?;:\"'()[]{}")

        if word in count:
            count[word] += 1
        else:
            count[word] = 1

    return count


def repeated_words(sentence):
    count = repetition_of_words(sentence)
    repeated = {}

    for word in count:
        if count[word] > 1:
            repeated[word] = count[word]

    return repeated


vowel_count = count_vowels(sentences)
consonant_count = count_consonants(sentences)
char_count = len(sentences)
longest = longest_word(sentences)
repetition_count = repetition_of_words(sentences)
repeated_word = repeated_words(sentences)


print(":" * 50)
print("Word Statistics and Word Analyzer")
print(":" * 50)
print(f"\nTotal number of words: {word_count}")
print(f"Total number of characters: {char_count}")
print(f"Total number of vowels: {vowel_count}")
print(f"Total number of consonants: {consonant_count}")
print(f"The longest word is: {longest}")
print(f"Word repetition count: {repetition_count}")
print(f"Repeated words are: {repeated_word} \n")
print(":" * 50)
