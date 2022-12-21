import preprocessing
import calculations
import simulations

file = preprocessing.read_file()
words_array = preprocessing.remove_symbols_and_create_array(file)


number_of_words = calculations.word_count(words_array)
print(number_of_words)
word_probs = calculations.calculate_word_probabilities(words_array)

bigrams = preprocessing.get_bigrams(words_array)

conditional_probabilities = calculations.conditional_probabilities(bigrams)


entropy = calculations.calculate_entropy(words_array)
print(entropy)

entropy_with_probability = calculations.calculate_entropy_with_probability(words_array, word_probs)
print(entropy_with_probability)
conditional_entropy = calculations.calculate_conditional_entropy(bigrams)
print(conditional_entropy)

markov_source = simulations.simulate_markov_source(word_probs,conditional_probabilities)
print(markov_source)