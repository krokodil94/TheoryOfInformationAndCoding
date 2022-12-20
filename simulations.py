import random

def simulate_markov_source(word_probs, conditional_probs):
    # Choose a random first word
    first_word = random.choices(list(word_probs.keys()), weights=word_probs.values())[0]
    words = [first_word]
    # Generate the rest of the words
    while True:
        # Get the possible next words and their probabilities
        next_word_probs = conditional_probs[words[-1]]
        next_words = [word for word, prob in next_word_probs.items() if word != "total_count"]
        probs = [prob for word, prob in next_word_probs.items() if word != "total_count"]
        # Stop if there are no possible next words
        if not next_words:
            break
        # Choose the next word based on the probabilities
        next_word = random.choices(next_words, weights=probs)[0]
        words.append(next_word)
        # Stop when the next word is not in the word_probs dictionary
        if next_word not in word_probs:
            break
    return words

