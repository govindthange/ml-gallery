import sys
import spacy
import pickle
import json

nlpModelPath = sys.argv[1]
text = sys.argv[2]

# Load the trained model from the pickle file
with open(nlpModelPath, "rb") as f:
    nlp = pickle.load(f)

# Process the text and return tagged entities
def process_text(text):
    doc = nlp(text)
    entities = [{"label": ent.label_, "text": ent.text} for ent in doc.ents]
    return json.dumps(entities)

def main():
    return process_text(text)

if __name__ == "__main__":
    print(main())
