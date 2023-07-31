import pandas as pd
import random
import spacy
from spacy.training import Example

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
nlp.to_disk("en_core_web_fin_sm")
# !zip -r /content/en_core_web_fin_sm.zip /content/en_core_web_fin_sm

# Test recommendations text
samples = [
  "ICICI Direct has buy call on Torrent Pharmaceuticals with a target price of Rs 2010.5. The current market price of Torrent Pharmaceuticals is Rs 1775.9. Time period given by analyst is a year when Torrent Pharmaceuticals price can reach defined target",
  "ICICI Direct has buy call on Punjab National Bank with a target price of Rs 52.4. The current market price of Punjab National Bank is Rs 51.48. Time period given by analyst is Intra Day when Punjab National Bank price can reach defined target. ICICI Direct recommended to keep stop loss at Rs 50.5",
  "ICICI Direct has buy call on Infosys with a target price of Rs 1335.8. The current market price of Infosys is Rs 1325.5. Time period given by analyst is Intra Day when Infosys price can reach defined target. ICICI Direct recommended to keep stop loss at Rs 1308.7",
  "HDFC Securities has buy call on Mahindra Holidays & Resorts India with a target price of Rs 360. The current market price of Mahindra Holidays & Resorts India is Rs 305.8. HDFC Securities recommended to keep stop loss at Rs 268",
  "Religare Broking has buy call on Coal India with a target price of Rs 260. The current market price of Coal India is Rs 246.7. Religare Broking recommended to keep stop loss at Rs 240",
  "Wall Street is enamoured with all things artificial intelligence (AI). Nowhere is this trend more evident than in the recent parabolic growth of graphics, computing, and networking solutions company Nvidia (NVDA 2.99%). Thanks to its central role as a pillar of global AI architecture, Nvidia has seen its market cap swell to nearly $1 trillion in 2023. For context, the graphics and cloud computing juggernaut started the year off with a far more modest market cap of approximately $350 billion."
]

# ML Test Prompt
while True:
  ip = input("\nEnter recommendation: ")
  if ip == "exit":
      break
  if ip == "show samples":
      for sample in samples:
        doc = nlp(sample)
        print("=> ", sample)
      continue
  elif ip == "test samples":
      for sample in samples:
        doc = nlp(sample)
        print("Sample: ", sample)
        for ent in doc.ents:
          print(ent.label_, '=', ent.text)
        print("\n")
      continue
  else:
    doc = nlp(ip)
    print("Recommendation: ", sample)
    for ent in doc.ents:
      print(ent.label_, '=', ent.text)
    print("\n")
