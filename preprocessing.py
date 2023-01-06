import string

# Open the file and read the text and make them all lowercase
def read_file():
    with open('test1.txt', 'r', encoding='utf-8') as f:
        return f.read().lower()


def remove_symbols_and_create_array(f):
    #remove all the symbols from the text using the string.punctuation
    #which contains all the common punctuation symbols.
    text = f.translate(str.maketrans('','',string.punctuation))
    # Split the text into words by whitespace
    words = text.split()
    return words

def get_bigrams(words):
  bigrams = [(words[i], words[i + 1]) for i in range(len(words) - 1)]
  return bigrams