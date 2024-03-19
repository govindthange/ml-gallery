# Development Environment (Core App)

### Prerequisite

Ensure you have brought up the 3 nlp-ner-trainer containers
```
govind@thinkpad:~/projects/ml-gallery/nlp-ner-trainer$ docker compose -f ./compose-dev.yaml up
```

## Step 1. Open `./nlp-ner-trainer/app` folder in VS Code

## Step 2. Attach it to the running app container

1. Click on `Attach to Running Container...`
2. Select `nlp-ner-trainer-app` container from the list.

## Step 3. Open container's `/app` folder in VS Code

## Step 4. Generate .pkl file

Train the model by running `train.py` script like so:
```
root@6116c1bb2f6e:/app# python train.py
root@6116c1bb2f6e:/app# 
```

It will generate the `nlp-ner-stck-recmndtns.pkl` in `/app/model` folder.

---

## Instructions

### Preprocessing

Step 1. Go to https://tecoholic.github.io/ner-annotator/

Step 2. `./training-data/preprocessed-data/sample.txt` file

Step 3. Create `tags` as per required labels.

Step 4. Annotate them by clicking on tag and then selecting the word(s) to be annotated.

Step 5. Go to `Annotations` menu and click `Export` menu to save annotations as JSON.

Step 6. Use this json content to populate `recommendations.csv` file.