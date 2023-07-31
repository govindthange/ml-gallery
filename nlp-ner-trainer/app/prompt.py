import spacy
import pandas as pd
import pickle

# Load the trained model from the pickle file
with open("./model/nlp-ner-stck-recmndtns.pkl", "rb") as f:
    nlp = pickle.load(f)

# ML Test Prompt
while True:
    ip = input("\nEnter recommendation: ")
    if ip == "exit":
        break
    if ip == "show samples":
        # Read the recommendations from the file using pandas
        sampleDataFrame = pd.read_csv("./training-data/test-samples.csv", header=None, names=["text"])
        samples = sampleDataFrame["text"].tolist()
        for sample in samples:
            doc = nlp(sample)
            print("=> ", sample)
        continue
    elif ip == "test samples":
        # Read the recommendations from the file using pandas
        sampleDataFrame = pd.read_csv("./training-data/test-samples.csv", header=None, names=["text"])
        samples = sampleDataFrame["text"].tolist()
        for sample in samples:
            doc = nlp(sample)
            print("Sample: ", sample)
            for ent in doc.ents:
                print(ent.label_, '=', ent.text)
            print("\n")
        continue
    else:
        doc = nlp(ip)
        print("Recommendation: ", ip)
        for ent in doc.ents:
            print(ent.label_, '=', ent.text)
        print("\n")
