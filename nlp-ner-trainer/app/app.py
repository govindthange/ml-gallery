import pandas as pd
import random
import spacy
from spacy.training import Example
import pickle

# Load en_core_web_sm which is a pre-trained English language model provided by the spaCy library.
# This model has been trained on a large corpus of text and contains word embeddings, 
# part-of-speech tagging, syntactic parsing, and named entity recognition capabilities.
nlp = spacy.load('en_core_web_sm')

# Add labels to to the model.
nlp.get_pipe('ner').add_label("STOCK")
nlp.get_pipe('ner').add_label("MARKET_PRICE")
nlp.get_pipe('ner').add_label("TARGET_PRICE")
nlp.get_pipe('ner').add_label("BUY_CALL")
nlp.get_pipe('ner').add_label("SELL_CALL")
nlp.get_pipe('ner').add_label("HOLD_CALL")
nlp.get_pipe('ner').add_label("STOP_LOSS")
nlp.get_pipe('ner').add_label("PERIOD")

# Load the training data from the CSV file using pandas
df = pd.read_csv("./training-data/recommendations.csv")

# Convert the DataFrame to a list of tuples (text, entities)
train_data = list(zip(df['text'], df['entities']))

# Convert the entities column from string representation to list of lists
train_data = [(text, {"entities": eval(entities)}) for text, entities in train_data]

# Train the NER model using random library

# https://spacy.io/usage/processing-pipelines
unaffected_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']

# The below code enhances the pre-trained model by adding custom entity labels like 
# "STOCK," "MARKET_PRICE," "TARGET_PRICE," etc., using the NER component provided by spaCy.
# Then, it fine-tunes the model using above custom dataset containing labeled examples of these entities in context.
with nlp.disable_pipes(*unaffected_pipes):
  optimizer = nlp.create_optimizer()
  
  # Adjust the number of iterations (i.e. 20) as needed
  for _ in range(20):
    random.shuffle(train_data)
    for text, annotations in train_data:
      doc = nlp.make_doc(text)
      example = Example.from_dict(doc, annotations)
      # Now we will train the existing en_core_web_sm, a pre-trained NLP model.
      nlp.update([example], sgd=optimizer)

# Save the model locally
nlp.to_disk("./model/en_core_web_fin_sm")

# Bundle the model in a single file using pickle
with open("./model/nlp-ner-stck-recmndtns.pkl", "wb") as f:
    pickle.dump(nlp, f)
