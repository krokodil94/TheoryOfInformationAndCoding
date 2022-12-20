import string
from collections import Counter
from collections import defaultdict
import math
from random import random
def read_file():
    with open('testsource.txt', 'r') as f:
        return f.read().lower()


def remove_symbols_and_create_array(f):
    #remove all the symbols from the text using the string.punctuation constant
    #which contains all the common punctuation symbols.
    text = f.translate(str.maketrans('','',string.punctuation))
    words = text.split()
    return words

def word_count(words):
  # Create an empty dictionary to store the counts
  counts = {}

  # Iterate over the words and count the number of occurrences of each word
  for word in words:
    if word in counts:
      counts[word] += 1
    else:
      counts[word] = 1

  # Return the number of words and the number of different words
  return len(words), len(counts)


def calculate_word_probabilities(words):

    # Use the Counter class to count the frequency of each word in the array.
    word_counts = Counter(words)

    # Calculate the probability of each word by dividing its frequency by the total number of words.
    total_words = sum(word_counts.values())
    word_probabilities = {word: count / total_words for word, count in word_counts.items()}

    return word_probabilities
print(calculate_word_probabilities(remove_symbols_and_create_array(read_file())))

def get_bigrams(words):
  bigrams = zip(words[:-1], words[1:])
  return list(bigrams)

def get_conditional_probabilities(biagrams):
    # Create a defaultdict to store the counts of each biagram
    biagram_counts = defaultdict(int)
    for biagram in biagrams:
        biagram_counts[biagram] += 1

    # Create a defaultdict to store the conditional probabilities of each second word given the first word in a biagram
    conditional_probabilities = defaultdict(dict)
    for biagram, count in biagram_counts.items():
        first_word, second_word = biagram
        # Increment the count for the first word
        conditional_probabilities[first_word]["total_count"] = conditional_probabilities[first_word].get("total_count", 0) + count
        # Increment the count for the second word given the first word
        conditional_probabilities[first_word][second_word] = conditional_probabilities[first_word].get(second_word, 0) + count

    # Calculate the conditional probabilities by dividing the count of each second word given the first word by the total count of the first word
    for first_word, second_word_counts in conditional_probabilities.items():
        total_count = second_word_counts["total_count"]
        for second_word, count in second_word_counts.items():
            if second_word == "total_count":
                continue
            conditional_probability = count / total_count
            conditional_probabilities[first_word][second_word] = conditional_probability

    return conditional_probabilities

def calculate_entropy(words):
    # Calculate the total number of words in the sequence
    num_words = len(words)

    # Calculate the probability of each word occurring in the sequence
    prob = [1 / num_words for _ in words]

    # Calculate the entropy of the sequence using the formula above
    entropy = -1 * sum(map(lambda x: x * math.log(x), prob))

    return entropy

def calculate_entropy_with_probability(words, probabilities):
    entropy = 0
    for i in probabilities.values():
        entropy += i * -math.log(i, 2)
    return entropy

def calculate_conditional_entropy(bigrams):
    # Count the number of occurrences of each word in the sequence
    word_counts = {}
    for bigram in bigrams:
        word1, word2 = bigram
        if word1 not in word_counts:
            word_counts[word1] = 0
        word_counts[word1] += 1

    # Calculate the conditional entropy of the sequence
    entropy = 0
    for bigram in bigrams:
        word1, word2 = bigram
        prob_word1 = word_counts[word1] / len(bigrams)
        entropy += prob_word1 * math.log2(1 / prob_word1)

    return entropy


def simulate_markov_source(probabilities, conditionals):
    # Get the first word by randomly selecting it according to its probability
    current_word = weighted_random(probabilities)
    message = [current_word]

    # Keep generating words until the end of the message is reached
    while current_word != "END":
        # Select the next word according to the conditional probabilities for the current word
        current_word = weighted_random(conditionals[current_word])
        message.append(current_word)

    return " ".join(message)


def weighted_random(word_probabilities):
    # Generate a random number between 0 and 1
    r = random()

    # Keep subtracting probabilities until a word is selected
    for word, probability in word_probabilities.items():
        r -= probability
        if r <= 0:
            return word