from collections import Counter
from collections import defaultdict
from math import log2

def word_count(words):
  # Count the number of occurrences of each word
  counts = Counter(words)

  total_number_of_words = len(words)
  unique_words = counts
  # Return the number of words and the number of different words
  return total_number_of_words,unique_words


def calculate_word_probabilities(words):
    number_of_words, word_counts = word_count(words)
    # Calculate the relative frequency (probability) of each word
    word_probabilities = {word: count / number_of_words for word, count in word_counts.items()}
    return word_probabilities



from collections import defaultdict

def conditional_probabilities(bigrams):
    # Create a defaultdict to store the counts of each bigram
    bigram_counts = defaultdict(int)
    for bigram in bigrams:
        bigram_counts[bigram] += 1

    # Create a defaultdict to store the conditional probabilities of each second word given the first word in a bigram
    conditional_probs = defaultdict(dict)
    for bigram, count in bigram_counts.items():
        first_word, second_word = bigram
        # Increment the count for the first word
        conditional_probs[first_word]["total_count"] = conditional_probs[first_word].get("total_count", 0) + count
        # Increment the count for the second word given the first word
        conditional_probs[first_word][second_word] = conditional_probs[first_word].get(second_word, 0) + count

    # Calculate the conditional probabilities by dividing the count of each second word given the first word by the total count of the first word
    for first_word, second_word_counts in conditional_probs.items():
        total_count = second_word_counts["total_count"]
        for second_word, count in second_word_counts.items():
            if second_word == "total_count":
                continue
            conditional_probability = count / total_count
            conditional_probs[first_word][second_word] = conditional_probability

    return conditional_probs



def calculate_entropy(words):
    # Calculate the probability of each word
    word_prob = 1 / len(words)
    # Calculate the entropy
    entropy = -sum(word_prob * log2(word_prob) for word in words)
    return entropy


def calculate_entropy_with_probability(words, word_probs):
    # Calculate the entropy
    entropy = -sum(prob * log2(prob) for prob in word_probs.values())
    return entropy

def calculate_conditional_entropy(bigrams):
    # Count the number of occurrences of each bigram
    bigram_counts = Counter(bigrams)
    # Calculate the probability of each bigram
    bigram_probs = {bigram: count/sum(bigram_counts.values()) for bigram, count in bigram_counts.items()}
    # Calculate the conditional probability of each second word given the first word
    conditional_probs = {}
    for bigram, prob in bigram_probs.items():
        first_word, second_word = bigram
        if first_word not in conditional_probs:
            conditional_probs[first_word] = {}
        total_prob = sum(bigram_probs.get((first_word, second_word), 0) for second_word in set(word for word, _ in bigrams))
        if total_prob > 0:
            conditional_probs[first_word][second_word] = prob/total_prob
    # Calculate the conditional entropy
    conditional_entropy = -sum(prob * log2(prob) for probs in conditional_probs.values() for prob in probs.values())
    return conditional_entropy


