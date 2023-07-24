# Import library for NLP
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

# Load the training data.
train_data = [
  ("Religare Broking has buy call on Coal India with a target price of Rs 260.3",{"entities":[[21,29,"BUY_CALL"],[33,43,"STOCK"],[70,75,"TARGET_PRICE"]]}),
  ("The current market price of Coal India is Rs 246.7",{"entities":[[28,38,"STOCK"],[45,50,"MARKET_PRICE"]]}),
  ("Religare Broking recommended to keep stop loss at Rs 240",{"entities":[[53,56,"STOP_LOSS"]]}),
  ("ICICI Direct has hold call on eClerx Services with a target price of Rs 1800.5",{"entities":[[17,26,"HOLD_CALL"],[30,45,"STOCK"],[72,78,"TARGET_PRICE"]]}),
  ("The current market price of eClerx Services is Rs 1587.9",{"entities":[[28,43,"STOCK"],[50,56,"MARKET_PRICE"]]}),
  ("Time period given by analyst is 12 months when eClerx Services Ltd. price can reach defined target",{"entities":[[32,41,"PERIOD"],[47,62,"STOCK"]]}),
  ("JM Financial has buy call on Rolex Rings with a target price of Rs 2500.5",{"entities":[[17,25,"BUY_CALL"],[29,40,"STOCK"],[67,73,"TARGET_PRICE"]]}),
  ("The current market price of Rolex Rings is Rs 1882.85",{"entities":[[28,39,"STOCK"],[46,53,"MARKET_PRICE"]]}),
  ("JM Financial has buy call on Archean Chemical Industries with a target price of Rs 810.1",{"entities":[[17,25,"BUY_CALL"],[29,56,"STOCK"],[83,88,"TARGET_PRICE"]]}),
  ("The current market price of Archean Chemical Industries is Rs 541.2",{"entities":[[28,55,"STOCK"],[62,67,"MARKET_PRICE"]]}),
  ("ICICI Direct has buy call on L&T Finance Holdings with a target price of Rs 104.6",{"entities":[[17,25,"BUY_CALL"],[29,40,"STOCK"],[76,81,"TARGET_PRICE"]]}),
  ("The current market price of L&T Finance Holdings is Rs 103.3.",{"entities":[[28,39,"STOCK"],[55,60,"MARKET_PRICE"]]}),
  ("Time period given by analyst is Intra Day when L&T Finance Holdings price can reach defined target",{"entities":[[47,58,"STOCK"]]}),
  ("ICICI Direct recommended to keep stoploss at Rs 102.2",{"entities":[[48,53,"STOP_LOSS"]]}),
  ("ICICI Direct has buy call on Tata Power Company with a target price of Rs 219.7",{"entities":[[17,25,"BUY_CALL"],[29,39,"STOCK"],[74,79,"TARGET_PRICE"]]}),
  ("The current market price of Tata Power Company is Rs 215.3",{"entities":[[28,38,"STOCK"],[53,58,"MARKET_PRICE"]]}),
  ("ICICI Direct recommended to keep stop loss at Rs 213.7.",{"entities":[[49,54,"STOP_LOSS"]]}),
  ("HDFC Securities is bullish on NCC has recommended buy rating on the stock with a target price of Rs 137 in its research report dated May 29, 2023",{"entities":[[30,33,"STOCK"],[100,103,"TARGET_PRICE"]]})
]

# Train the NER model
import random

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

for sample in samples:
  doc = nlp(sample)
  print("Sample: ", sample)
  for ent in doc.ents:
    print(ent.label_, '=', ent.text)
  print("\n")
