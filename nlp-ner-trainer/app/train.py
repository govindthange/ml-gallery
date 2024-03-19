import pandas as pd
import random
import spacy
from spacy.training import Example
import pickle

# Load en_core_web_sm which is a pre-trained English language model provided by the spaCy library.
# This model has been trained on a large corpus of text and contains word embeddings, 
# part-of-speech tagging, syntactic parsing, and named entity recognition capabilities.
#  - en: indicates that the model is for the English language.
#  - core: signifies that the model is a foundational part of spaCy's available models.
#  - web: tells that the model is trained on a diverse range of text data from the web.
#  - sm: stands for "small," indicating that the model is compact/lightweight version of the English language model within the spaCy library.

# Use nlp variable to hold the spaCy language processing pipeline.
#  - This pipeline includes components such as tokenization, part-of-speech tagging, dependency parsing, and named entity recognition (NER).
#  - NER is a process in natural language processing that involves identifying and classifying named entities
#    (such as names of people, organizations, dates, and more) in text.
nlp = spacy.load('en_core_web_sm')

# We retrieve NER component from the spaCy pipeline using get_pipe('ner')
# We add a custom label to NER component using .add_label("STOCK")
# The label indicates that the NER component will be trained to recognize and classify text spans that are related to stocks.
# With this NER model will be able to recognize and classify text spans that refer to stocks.
nlp.get_pipe('ner').add_label("STOCK")
nlp.get_pipe('ner').add_label("MARKET_PRICE")
nlp.get_pipe('ner').add_label("TARGET_PRICE")
nlp.get_pipe('ner').add_label("BUY_CALL")
nlp.get_pipe('ner').add_label("SELL_CALL")
nlp.get_pipe('ner').add_label("HOLD_CALL")
nlp.get_pipe('ner').add_label("STOP_LOSS")
nlp.get_pipe('ner').add_label("PERIOD")

# Follow ./README.md instructions to prepare training data.
# Load the training data from the CSV file using pandas
df = pd.read_csv("./training-data/recommendations.csv")

# Convert the DataFrame to a list of tuples (text, entities)
train_data = list(zip(df['text'], df['entities']))

# Convert the entities column from string representation to list of lists
train_data = [(text, {"entities": eval(entities)}) for text, entities in train_data]

# Train the NER model using random library

# https://spacy.io/usage/processing-pipelines
# nlp.pipe_names list contains the names of all pipeline components of the spaCy model
# Filter/remove 'ner' component from the list of pipeline components in nlp.pipe_names
unaffected_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']

# The below code enhances the pre-trained model by adding custom entity labels like 
# "STOCK," "MARKET_PRICE," "TARGET_PRICE," etc., using the NER component provided by spaCy.
# Then, it fine-tunes the model using above custom dataset containing labeled examples of these entities in context.

# use 'with' statement to ensure that only 'ner' component is updated during training and other components remain unchanged,
# Following line will temporarily disable the pipeline components that are required to be unaffected.
with nlp.disable_pipes(*unaffected_pipes):

  # Creates optimizer for updating model's parameters during training
  optimizer = nlp.create_optimizer()
  
  # WARNING: Since we don't have training data we shuffle and iterate through the same list.
  # This is not recommended!
  for _ in range(20):
    random.shuffle(train_data)
    for text, annotations in train_data:
      # converts text into a spaCy Doc object
      doc = nlp.make_doc(text)
      # Prepare training example in the required format for updating the NER model.
      example = Example.from_dict(doc, annotations)
      # Now train the existing en_core_web_sm, a pre-trained NLP model.
      # Update the NER model using the training example
      nlp.update([example], sgd=optimizer)

# Save the model locally
nlp.to_disk("./model/en_core_web_fin_sm")

# Bundle the model in a single file using pickle
with open("./model/nlp-ner-stck-recmndtns.pkl", "wb") as f:
    pickle.dump(nlp, f)
