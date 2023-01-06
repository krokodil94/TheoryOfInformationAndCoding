from collections import Counter
from collections import defaultdict
from math import log2

def word_count(words):
    # Return the total number of words, and the dictionary of unique words and their counts
  return len(words),Counter(words)


def calculate_word_probabilities(words):
  # Calculate the relative frequency (probability) of each word
  return {word: count / len(words) for word, count in Counter(words).items()}


def conditional_probabilities(bigrams):
    # Create a defaultdict to store the counts of each bigram
    bigram_counts = defaultdict(int)
    for bigram in bigrams:
        bigram_counts[bigram] += 1

    # Create a dictionary to store the conditional probabilities of each second word given the first word in a bigram
    conditional_probs = {}
    # Iterate over the bigram_counts dictionary and increment the count for the first word and the count for the second word given the first word in the conditional_probs dictionary
    for bigram, count in bigram_counts.items():
        first_word, second_word = bigram
        # Ensure that the dictionary includes an entry for the first word
        if first_word not in conditional_probs:
            conditional_probs[first_word] = {}
        # Increment the count for the second word given the first word
        conditional_probs[first_word][second_word] = conditional_probs[first_word].get(second_word, 0) + count

    # Calculate the conditional probabilities by dividing the count of each second word given the first word by the total count of the first word
    for first_word, second_word_counts in conditional_probs.items():
        total_count = sum(count for count in second_word_counts.values())
        for second_word, count in second_word_counts.items():
            conditional_probability = count / total_count
            conditional_probs[first_word][second_word] = conditional_probability

    return conditional_probs





def calculate_entropy(words):
    # Calculate the probability of each word
    word_prob = 1 / len(set(words))
    # Calculate the entropy
    entropy = -log2(word_prob)
    return entropy


def calculate_entropy_with_probability(word_probs):
    # Calculate the entropy

    entropy = -sum(prob * log2(prob) for prob in word_probs.values())
    return entropy

def calculate_conditional_entropy(conditional_probs, word_probs):
    # Calculate the conditional entropy
    conditional_entropy = 0
    for first_word, second_word_probs in conditional_probs.items():
        first_word_prob = word_probs[first_word]

        for second_word, prob in second_word_probs.items():
            conditional_entropy += first_word_prob * prob * log2(1/prob)
    return conditional_entropy








