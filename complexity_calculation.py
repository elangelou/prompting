
import pandas as pd

from textstat import flesch_kincaid_grade

# Input sentences 
sentences = [
    "Compassion",
    "Compassion is good",
    "Compassion is a moral virtue",
    "I try to show compassion whenever I can",
    "Let me tell you what I think about showing compassion",
    "I believe that compassion is the highest of all virtues",
    "Compassion is the greatest virtue",
    "I will show compassion to everyone who needs it",
    "I always show compassion to my friends",
    "Please have some compassion and help them"
]

# Custom function to estimate sentence complexity
def estimate_complexity(sentence):
    # Complexity based on the number of words and commas
    num_words = len(sentence.split())
    num_commas = sentence.count(',')
    return num_words + num_commas

# Create a list of tuples containing each sentence and its estimated complexity
sentence_complexity = [(sentence, estimate_complexity(sentence)) for sentence in sentences]

# Sort the sentences by their complexity score and length
sorted_sentences = sorted(sentence_complexity, key=lambda x: (x[1], len(x[0])))

# Creating a DataFrame to store the sorted sentences and their attributes
sentence_df = pd.DataFrame(sorted_sentences, columns=['Sentence', 'Complexity'])

# Convert the DataFrame into a matrix
sentence_matrix = sentence_df.values.tolist()
sentence_matrix